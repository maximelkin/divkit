import type { Readable, Writable } from 'svelte/types/runtime/store';
import type { WrappedError } from '../utils/wrapError';
import type { Action, DivBase, DivExtension, DivExtensionContext, TemplateContext } from '../../typings/common';
import type { VisibilityAction } from '../types/visibilityAction';
import type { DivBaseData } from '../types/base';
import type { MaybeMissing } from '../expressions/json';
import type { Variable, VariableType } from '../expressions/variable';
import type { TintMode } from '../types/image';
import type { Customization } from '../../typings/common';

export const ROOT_CTX = Symbol('root');

export type Running = 'stateChange';

export interface RootCtxValue {
    logError(error: WrappedError): void;
    logStat(type: string, action: MaybeMissing<Action | VisibilityAction>): void;
    hasTemplate(templateName: string): boolean;
    processTemplate(json: DivBaseData, templateContext: TemplateContext): {
        json: DivBaseData;
        templateContext: TemplateContext;
    };
    genId(key: string): string;
    genClass(key: string): string;
    execAction(action: MaybeMissing<Action | VisibilityAction>): void;
    execAnyActions(actions: MaybeMissing<Action[]> | undefined, processUrls?: boolean): Promise<void>;
    execCustomAction(action: (Action | VisibilityAction) & { url: string }): void;
    isRunning(type: Running): boolean;
    setRunning(type: Running, val: boolean): void;
    registerInstance<T>(id: string, block: T): void;
    unregisterInstance(id: string): void;
    addSvgFilter(color: string, mode: TintMode): string;
    removeSvgFilter(color: string | undefined, mode: TintMode): void;
    getDerivedFromVars<T>(jsonProp: T): Readable<MaybeMissing<T>>;
    getJsonWithVars<T>(jsonProp: T): MaybeMissing<T>;
    getStore<T>(id: string): Writable<T>;
    getVariable(varName: string, type: VariableType): Variable | undefined;
    getCustomization<K extends keyof Customization>(prop: K): Customization[K] | undefined;
    getBuiltinProtocols(): Set<string>;
    getExtension(id: string, params: object | undefined): DivExtension | undefined;
    getExtensionContext(): DivExtensionContext;
    isDesktop: Readable<boolean>;

    // Devtool
    registerComponent?({
        node,
        json,
        origJson,
        templateContext
    }: {
        node: HTMLElement;
        json: Partial<DivBaseData>;
        origJson: DivBase | undefined;
        templateContext: TemplateContext;
    }): void;
    unregisterComponent?({
        node
    }: {
        node: HTMLElement;
    }): void;
}
