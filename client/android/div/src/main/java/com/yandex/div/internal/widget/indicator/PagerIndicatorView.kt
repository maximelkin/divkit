package com.yandex.div.internal.widget.indicator

import android.content.Context
import android.graphics.Canvas
import android.util.AttributeSet
import android.view.View
import androidx.viewpager2.widget.ViewPager2
import com.yandex.div.internal.widget.indicator.animations.getIndicatorAnimator
import com.yandex.div.internal.widget.indicator.forms.getIndicatorDrawer
import kotlin.math.min

internal open class PagerIndicatorView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : View(context, attrs, defStyleAttr) {

    private var stripDrawer: IndicatorsStripDrawer? = null
    private var pager: ViewPager2? = null
    private var style: IndicatorParams.Style? = null

    private val onPageChangeListener: ViewPager2.OnPageChangeCallback = object: ViewPager2.OnPageChangeCallback() {
        override fun onPageScrolled(position: Int, positionOffset: Float, positionOffsetPixels: Int) {
            stripDrawer?.let {
                // ViewPager may emit negative positionOffset for very fast scrolling
                val offset = when {
                    positionOffset < 0 -> 0f
                    positionOffset > 1 -> 1f
                    else -> positionOffset
                }
                it.onPageScrolled(position, offset)
                invalidate()
            }
        }

        override fun onPageSelected(position: Int) {
            stripDrawer?.let {
                it.onPageSelected(position)
                invalidate()
            }
        }
    }

    fun setStyle(style: IndicatorParams.Style) {
        this.style = style

        stripDrawer = IndicatorsStripDrawer(style, getIndicatorDrawer(style), getIndicatorAnimator(style)).apply {
            calculateMaximumVisibleItems(
                measuredWidth - paddingLeft - paddingRight,
                measuredHeight - paddingTop - paddingBottom
            )
            update()
        }

        requestLayout()
    }

    override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
        val heightMode = MeasureSpec.getMode(heightMeasureSpec)
        val heightSize = MeasureSpec.getSize(heightMeasureSpec)
        val selectedHeight = style?.activeShape?.itemSize?.height ?: 0f
        val desiredHeight = (selectedHeight + paddingTop + paddingBottom).toInt()
        val measuredHeight = when (heightMode) {
            MeasureSpec.EXACTLY -> heightSize
            MeasureSpec.AT_MOST -> min(desiredHeight, heightSize)
            MeasureSpec.UNSPECIFIED -> desiredHeight
            else -> desiredHeight
        }

        val widthMode = MeasureSpec.getMode(widthMeasureSpec)
        val widthSize = MeasureSpec.getSize(widthMeasureSpec)
        val selectedWidth = style?.activeShape?.itemSize?.width ?: 0f
        val desiredWidth = when (val itemPlacement = style?.itemsPlacement) {
            is IndicatorParams.ItemPlacement.Default ->
                (itemPlacement.spaceBetweenCenters * (pager?.adapter?.itemCount ?: 0) + selectedWidth).toInt() + paddingLeft + paddingRight
            is IndicatorParams.ItemPlacement.Stretch -> widthSize
            null -> selectedWidth.toInt() + paddingLeft + paddingRight
        }
        val measuredWidth = when (widthMode) {
            MeasureSpec.EXACTLY -> widthSize
            MeasureSpec.AT_MOST -> min(desiredWidth, widthSize)
            MeasureSpec.UNSPECIFIED -> desiredWidth
            else -> desiredWidth
        }
        setMeasuredDimension(measuredWidth, measuredHeight)

        stripDrawer?.calculateMaximumVisibleItems(
            measuredWidth - paddingLeft - paddingRight,
            measuredHeight - paddingTop - paddingBottom
        )
    }

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)
        canvas.translate(paddingLeft.toFloat(), paddingTop.toFloat())
        stripDrawer?.onDraw(canvas)
    }

    fun attachPager(newPager: ViewPager2) {
        if (pager === newPager) {
            return
        }

        pager?.unregisterOnPageChangeCallback(onPageChangeListener)

        pager = newPager.apply {
            requireNotNull(adapter) { "Attached pager adapter is null!" }
            registerOnPageChangeCallback(onPageChangeListener)
        }

        stripDrawer?.update()
    }

    private fun IndicatorsStripDrawer.update() {
        pager?.let {
            it.adapter?.let { adapter ->
                setItemsCount(adapter.itemCount)
            }
            onPageSelected(it.currentItem)
            invalidate()
        }
    }
}
