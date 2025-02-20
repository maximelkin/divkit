package com.yandex.div.video.custom

import android.content.Context
import android.graphics.Color
import android.graphics.PixelFormat
import android.view.SurfaceView
import android.view.ViewGroup.LayoutParams.MATCH_PARENT
import android.widget.FrameLayout
import android.widget.ImageView
import androidx.core.view.isVisible
import com.google.android.exoplayer2.ExoPlaybackException
import com.google.android.exoplayer2.Player
import com.google.android.exoplayer2.Player.DISCONTINUITY_REASON_AUTO_TRANSITION
import com.google.android.exoplayer2.ui.PlayerView
import com.yandex.div.internal.KAssert
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.MainScope
import kotlinx.coroutines.cancel
import kotlinx.coroutines.cancelChildren
import kotlinx.coroutines.launch

internal class VideoView(
    context: Context,
    zOrderMode: ZOrderMode = ZOrderMode.ON_TOP,
) : FrameLayout(context) {
    private val coroutineScope: CoroutineScope = MainScope()
    private var stubViewObservationJob: Job? = null

    var viewModel: VideoViewModel? = null
        private set

    private val playerView = PlayerView(context).apply {
        useController = false
        setShutterBackgroundColor(Color.TRANSPARENT)
        (videoSurfaceView as? SurfaceView)?.apply {
            when (zOrderMode) {
                ZOrderMode.ON_TOP -> setZOrderOnTop(true)
                ZOrderMode.MEDIA_OVERLAY -> setZOrderMediaOverlay(true)
            }
            setBackgroundColor(Color.TRANSPARENT)
            holder.setFormat(PixelFormat.TRANSPARENT)
        }
    }

    private val stubImageView: ImageView = ImageView(context).apply {
        layoutParams = LayoutParams(MATCH_PARENT, MATCH_PARENT)
        scaleType = ImageView.ScaleType.FIT_CENTER
        isVisible = false
        setBackgroundColor(Color.TRANSPARENT)
    }

    init {
        addView(stubImageView)
        addView(playerView)
    }

    private val playerListener = object : Player.Listener {
        override fun onPositionDiscontinuity(
            oldPosition: Player.PositionInfo,
            newPosition: Player.PositionInfo,
            reason: Int
        ) {
            if (reason == DISCONTINUITY_REASON_AUTO_TRANSITION) {
                // Video has ended and now is repeating
                assertBoundToViewModel()
                viewModel?.onVideoRepeat()
            }
        }

        override fun onRenderedFirstFrame() {
            assertBoundToViewModel()
            viewModel?.onVideoStartedShowing()
        }

        override fun onPlayerError(error: ExoPlaybackException) {
            assertBoundToViewModel()
            viewModel?.onPlaybackError(error)
        }
    }

    fun bindToViewModel(model: VideoViewModel) {
        viewModel?.let { pauseObservingViewModel(it) }
        stubImageView.setImageBitmap(null)
        stubImageView.isVisible = false

        viewModel = model

        if (isAttachedToWindow) {
            resumeObservingViewModel(model)
        }
    }

    private fun assertBoundToViewModel() {
        if (viewModel == null) {
            KAssert.fail { "VideoView is required to be bound to view model, but it isn't bound" }
        }
    }

    private fun observeStubViewState(model: VideoViewModel): Job =
        coroutineScope.launch(Dispatchers.Main.immediate) {
            model.stubImageIfVisible.collect { image ->
                stubImageView.setImageBitmap(image)
                stubImageView.isVisible = image != null
            }
        }

    private fun resumeObservingViewModel(model: VideoViewModel) {
        playerView.player = model.player
        model.player.addListener(playerListener)
        model.unfreezePlayback()
        stubViewObservationJob?.cancel()
        stubViewObservationJob = observeStubViewState(model)
    }

    private fun pauseObservingViewModel(model: VideoViewModel) {
        playerView.player = null
        model.player.removeListener(playerListener)
        model.freezePlayback()
        coroutineScope.coroutineContext.cancelChildren()
        stubViewObservationJob = null
    }

    override fun onAttachedToWindow() {
        super.onAttachedToWindow()
        assertBoundToViewModel()
        viewModel?.let { resumeObservingViewModel(it) }
    }

    override fun onDetachedFromWindow() {
        super.onDetachedFromWindow()
        viewModel?.let { pauseObservingViewModel(it) }
    }

    fun release() {
        viewModel?.let { pauseObservingViewModel(it) }
        coroutineScope.cancel()
        playerView.player = null
        viewModel = null
    }
}
