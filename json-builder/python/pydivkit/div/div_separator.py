# Generated code. Do not modify.
# flake8: noqa: F401, F405, F811

from __future__ import annotations

import enum
import typing

from pydivkit.core import BaseDiv, Field

from . import (
    div_accessibility, div_action, div_alignment_horizontal,
    div_alignment_vertical, div_animation, div_appearance_transition,
    div_background, div_border, div_change_transition, div_edge_insets,
    div_extension, div_focus, div_size, div_tooltip, div_transform,
    div_transition_trigger, div_visibility, div_visibility_action,
)


# A separating line between elements.
class DivSeparator(BaseDiv):

    def __init__(
        self, *,
        type: str = "separator",
        accessibility: typing.Optional[div_accessibility.DivAccessibility] = None,
        action: typing.Optional[div_action.DivAction] = None,
        action_animation: typing.Optional[div_animation.DivAnimation] = None,
        actions: typing.Optional[typing.List[div_action.DivAction]] = None,
        alignment_horizontal: typing.Optional[div_alignment_horizontal.DivAlignmentHorizontal] = None,
        alignment_vertical: typing.Optional[div_alignment_vertical.DivAlignmentVertical] = None,
        alpha: typing.Optional[float] = None,
        background: typing.Optional[typing.List[div_background.DivBackground]] = None,
        border: typing.Optional[div_border.DivBorder] = None,
        column_span: typing.Optional[int] = None,
        delimiter_style: typing.Optional[DivSeparatorDelimiterStyle] = None,
        doubletap_actions: typing.Optional[typing.List[div_action.DivAction]] = None,
        extensions: typing.Optional[typing.List[div_extension.DivExtension]] = None,
        focus: typing.Optional[div_focus.DivFocus] = None,
        height: typing.Optional[div_size.DivSize] = None,
        id: typing.Optional[str] = None,
        longtap_actions: typing.Optional[typing.List[div_action.DivAction]] = None,
        margins: typing.Optional[div_edge_insets.DivEdgeInsets] = None,
        paddings: typing.Optional[div_edge_insets.DivEdgeInsets] = None,
        row_span: typing.Optional[int] = None,
        selected_actions: typing.Optional[typing.List[div_action.DivAction]] = None,
        tooltips: typing.Optional[typing.List[div_tooltip.DivTooltip]] = None,
        transform: typing.Optional[div_transform.DivTransform] = None,
        transition_change: typing.Optional[div_change_transition.DivChangeTransition] = None,
        transition_in: typing.Optional[div_appearance_transition.DivAppearanceTransition] = None,
        transition_out: typing.Optional[div_appearance_transition.DivAppearanceTransition] = None,
        transition_triggers: typing.Optional[typing.List[div_transition_trigger.DivTransitionTrigger]] = None,
        visibility: typing.Optional[div_visibility.DivVisibility] = None,
        visibility_action: typing.Optional[div_visibility_action.DivVisibilityAction] = None,
        visibility_actions: typing.Optional[typing.List[div_visibility_action.DivVisibilityAction]] = None,
        width: typing.Optional[div_size.DivSize] = None,
    ):
        super().__init__(
            type=type,
            accessibility=accessibility,
            action=action,
            action_animation=action_animation,
            actions=actions,
            alignment_horizontal=alignment_horizontal,
            alignment_vertical=alignment_vertical,
            alpha=alpha,
            background=background,
            border=border,
            column_span=column_span,
            delimiter_style=delimiter_style,
            doubletap_actions=doubletap_actions,
            extensions=extensions,
            focus=focus,
            height=height,
            id=id,
            longtap_actions=longtap_actions,
            margins=margins,
            paddings=paddings,
            row_span=row_span,
            selected_actions=selected_actions,
            tooltips=tooltips,
            transform=transform,
            transition_change=transition_change,
            transition_in=transition_in,
            transition_out=transition_out,
            transition_triggers=transition_triggers,
            visibility=visibility,
            visibility_action=visibility_action,
            visibility_actions=visibility_actions,
            width=width,
        )

    type: str = Field(default="separator")
    accessibility: typing.Optional[div_accessibility.DivAccessibility] = Field(
        description="Accessibility for disabled people.",
    )
    action: typing.Optional[div_action.DivAction] = Field(
        description=(
            "One action when clicking on an element. Not used if the "
            "`actions` parameter isset."
        ),
    )
    action_animation: typing.Optional[div_animation.DivAnimation] = Field(
        description=(
            "Action animation. Web supports `fade`, `scale` and `set` "
            "only."
        ),
    )
    actions: typing.Optional[typing.List[div_action.DivAction]] = Field(
        min_items=1, 
        description="Multiple actions when clicking on an element.",
    )
    alignment_horizontal: typing.Optional[div_alignment_horizontal.DivAlignmentHorizontal] = Field(
        description=(
            "Horizontal alignment of an element inside the parent "
            "element."
        ),
    )
    alignment_vertical: typing.Optional[div_alignment_vertical.DivAlignmentVertical] = Field(
        description=(
            "Vertical alignment of an element inside the parent element."
        ),
    )
    alpha: typing.Optional[float] = Field(
        description=(
            "Sets transparency of the entire element: `0` — completely "
            "transparent, `1` —opaque."
        ),
    )
    background: typing.Optional[typing.List[div_background.DivBackground]] = Field(
        min_items=1, 
        description="Element background. It can contain multiple layers.",
    )
    border: typing.Optional[div_border.DivBorder] = Field(
        description="Element stroke.",
    )
    column_span: typing.Optional[int] = Field(
        description=(
            "Merges cells in a column of the [grid](div-grid.md) "
            "element."
        ),
    )
    delimiter_style: typing.Optional[DivSeparatorDelimiterStyle] = Field(
        description="Separator display settings.",
    )
    doubletap_actions: typing.Optional[typing.List[div_action.DivAction]] = Field(
        min_items=1, 
        description="Action when double-clicking on an element.",
    )
    extensions: typing.Optional[typing.List[div_extension.DivExtension]] = Field(
        min_items=1, 
        description=(
            "Extensions for additional processing of an element. The "
            "list of extensions isgiven in "
            "[DivExtension](../../extensions.dita)."
        ),
    )
    focus: typing.Optional[div_focus.DivFocus] = Field(
        description="Parameters when focusing on an element or losing focus.",
    )
    height: typing.Optional[div_size.DivSize] = Field(
        description=(
            "Element height. For Android: if there is text in this or in "
            "a child element,specify height in `sp` to scale the element "
            "together with the text. To learn moreabout units of size "
            "measurement, see [Layout inside the "
            "card](../../layout.dita)."
        ),
    )
    id: typing.Optional[str] = Field(
        min_length=1, 
        description=(
            "Element ID. It must be unique within the root element. It "
            "is used as`accessibilityIdentifier` on iOS."
        ),
    )
    longtap_actions: typing.Optional[typing.List[div_action.DivAction]] = Field(
        min_items=1, 
        description=(
            "Action when long-clicking on an element. Doesn\'t work on "
            "the devices w/o touchgestures."
        ),
    )
    margins: typing.Optional[div_edge_insets.DivEdgeInsets] = Field(
        description="External margins from the element stroke.",
    )
    paddings: typing.Optional[div_edge_insets.DivEdgeInsets] = Field(
        description="Internal margins from the element stroke.",
    )
    row_span: typing.Optional[int] = Field(
        description=(
            "Merges cells in a string of the [grid](div-grid.md) "
            "element."
        ),
    )
    selected_actions: typing.Optional[typing.List[div_action.DivAction]] = Field(
        min_items=1, 
        description=(
            "List of [actions](div-action.md) to be executed when "
            "selecting an element in[pager](div-pager.md)."
        ),
    )
    tooltips: typing.Optional[typing.List[div_tooltip.DivTooltip]] = Field(
        min_items=1, 
        description=(
            "Tooltips linked to an element. A tooltip can be shown "
            "by`div-action://show_tooltip?id=`, hidden by "
            "`div-action://hide_tooltip?id=` where`id` — tooltip id."
        ),
    )
    transform: typing.Optional[div_transform.DivTransform] = Field(
        description=(
            "Transformation of the element. Applies the passed transform "
            "to the element. Thecontent that does not fit into the "
            "original view will be cut off."
        ),
    )
    transition_change: typing.Optional[div_change_transition.DivChangeTransition] = Field(
        description=(
            "Change animation. It is played when the position or size of "
            "an element changes inthe new layout."
        ),
    )
    transition_in: typing.Optional[div_appearance_transition.DivAppearanceTransition] = Field(
        description=(
            "Appearance animation. It is played when an element with a "
            "new ID appears. Tolearn more about the concept of "
            "transitions, see "
            "[Animatedtransitions](../../interaction.dita#animation/tran"
            "sition-animation)."
        ),
    )
    transition_out: typing.Optional[div_appearance_transition.DivAppearanceTransition] = Field(
        description=(
            "Disappearance animation. It is played when an element "
            "disappears in the newlayout."
        ),
    )
    transition_triggers: typing.Optional[typing.List[div_transition_trigger.DivTransitionTrigger]] = Field(
        min_items=1, 
        description=(
            "Animation starting triggers. Default value: `[state_change, "
            "visibility_change]`."
        ),
    )
    visibility: typing.Optional[div_visibility.DivVisibility] = Field(
        description="Element visibility.",
    )
    visibility_action: typing.Optional[div_visibility_action.DivVisibilityAction] = Field(
        description=(
            "Tracking visibility of a single element. Not used if the "
            "`visibility_actions`parameter is set."
        ),
    )
    visibility_actions: typing.Optional[typing.List[div_visibility_action.DivVisibilityAction]] = Field(
        min_items=1, 
        description="Actions when an element appears on the screen.",
    )
    width: typing.Optional[div_size.DivSize] = Field(
        description="Element width.",
    )


# Separator display settings.
class DivSeparatorDelimiterStyle(BaseDiv):

    def __init__(
        self, *,
        color: typing.Optional[str] = None,
        orientation: typing.Optional[DelimiterStyleOrientation] = None,
    ):
        super().__init__(
            color=color,
            orientation=orientation,
        )

    color: typing.Optional[str] = Field(
        format="color", 
        description=(
            "Separator color. To prevent the separator from being "
            "displayed, set transparencyin the alpha channel. For "
            "example, `#00FFFFFF`."
        ),
    )
    orientation: typing.Optional[DelimiterStyleOrientation] = Field(
        description=(
            "Separator orientation:`vertical` — vertical;`horizontal` — "
            "horizontal.<"
        ),
    )


class DelimiterStyleOrientation(str, enum.Enum):
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"


DivSeparatorDelimiterStyle.update_forward_refs()


DivSeparator.update_forward_refs()
