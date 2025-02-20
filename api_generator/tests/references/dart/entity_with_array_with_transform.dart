// Generated code. Do not modify.

import 'package:equatable/equatable.dart';

import '../utils/parsing_extensions.dart';

class EntityWithArrayWithTransform with EquatableMixin {
  const EntityWithArrayWithTransform({
    required this.array,
  });

  static const type = "entity_with_array_with_transform";
  // at least 1 elements
  final List<int> array;

  @override
  List<Object?> get props => [
        array,
      ];

  static EntityWithArrayWithTransform? fromJson(Map<String, dynamic>? json) {
    if (json == null) {
      return null;
    }
    return EntityWithArrayWithTransform(
      array: (json['array'] as List<dynamic>).map((v) => (v as int)).toList(),
    );
  }
}
