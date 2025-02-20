import type { VisibilityAction } from '../types/visibilityAction';
import type { MaybeMissing } from '../expressions/json';
import { RootCtxValue } from '../context/root';
import { getUrlSchema, isBuiltinSchema } from '../utils/url';

export function visibilityAction(node: HTMLElement, {
    visibilityActions,
    rootCtx
}: {
    visibilityActions: VisibilityAction[];
    rootCtx: RootCtxValue;
}) {
    const visibilityStatus: {
        index: number;
        action: VisibilityAction;
        visible: boolean;
        count: number;
        finished: boolean;
        timer?: ReturnType<typeof setTimeout>;
    }[] = visibilityActions.map((it, index) => ({
        index,
        action: it,
        visible: false,
        count: 0,
        finished: false
    }));

    const calcedList = visibilityActions.map(it => rootCtx.getJsonWithVars({
        visibility_percentage: it.visibility_percentage,
        visibility_duration: it.visibility_duration,
        log_limit: it.log_limit
    }));

    const thresholds = [...new Set([...visibilityActions.map((it, index) =>
        (calcedList[index].visibility_percentage || 50) / 100
    )])];

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            visibilityStatus.forEach(status => {
                const nowVisible = entry.intersectionRatio >= (status.action.visibility_percentage || 50) / 100;

                if (!status.visible && nowVisible) {
                    if (!status.finished) {
                        status.timer = setTimeout(() => {
                            ++status.count;

                            const calcedParams = calcedList[status.index];
                            const limit = calcedParams.log_limit === 0 ? Infinity : (calcedParams.log_limit || 1);
                            if (++status.count >= limit) {
                                status.finished = true;
                            }

                            const calcedAction = rootCtx.getJsonWithVars(status.action);
                            const actionUrl = calcedAction.url;
                            if (actionUrl) {
                                const schema = getUrlSchema(actionUrl);
                                if (schema && !isBuiltinSchema(schema, rootCtx.getBuiltinProtocols())) {
                                    if (schema === 'div-action') {
                                        rootCtx.execAction(calcedAction);
                                    } else if (calcedAction.log_id) {
                                        rootCtx.execCustomAction(calcedAction as VisibilityAction & { url: string });
                                    }
                                }
                            }

                            rootCtx.logStat('visible', calcedAction);
                        }, calcedList[status.index].visibility_duration || 800);
                    }
                } else if (!nowVisible) {
                    if (status.timer) {
                        clearTimeout(status.timer);
                    }
                }
                status.visible = nowVisible;
            });
        });
    }, {
        threshold: thresholds
    });

    observer.observe(node);

    return {
        destroy() {
            observer.disconnect();

            visibilityStatus.forEach(status => {
                if (status.timer) {
                    clearTimeout(status.timer);
                }
            });
        }
    };
}
