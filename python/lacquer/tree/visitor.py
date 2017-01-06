from .join_criteria import JoinOn


class AstVisitor(object):
    def __init__(self, line=None, pos=None):
        self.line = line
        self.pos = pos

    def process(self, node, context):
        return node.accept(self, context)

    def visit_node(self, node, context):
        pass

    def visit_expression(self, node, context):
        return self.visit_node(node, context)

    def visit_reset_session(self, node, context):
        return self.visit_statement(node, context)

    def visit_current_time(self, node, context):
        return self.visit_expression(node, context)

    def visit_extract(self, node, context):
        return self.visit_expression(node, context)

    def visit_arithmetic_binary(self, node, context):
        return self.visit_expression(node, context)

    def visit_between_predicate(self, node, context):
        return self.visit_expression(node, context)

    def visit_coalesce_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_comparison_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_literal(self, node, context):
        return self.visit_expression(node, context)

    def visit_double_literal(self, node, context):
        return self.visit_literal(node, context)

    def visit_statement(self, node, context):
        return self.visit_node(node, context)

    def visit_query(self, node, context):
        return self.visit_statement(node, context)

    def visit_explain(self, node, context):
        return self.visit_statement(node, context)

    def visit_show_tables(self, node, context):
        return self.visit_statement(node, context)

    def visit_show_schemas(self, node, context):
        return self.visit_statement(node, context)

    def visit_show_catalogs(self, node, context):
        return self.visit_statement(node, context)

    def visit_show_columns(self, node, context):
        return self.visit_statement(node, context)

    def visit_show_partitions(self, node, context):
        return self.visit_statement(node, context)

    def visit_show_functions(self, node, context):
        return self.visit_statement(node, context)

    def visit_use(self, node, context):
        return self.visit_statement(node, context)

    def visit_show_session(self, node, context):
        return self.visit_statement(node, context)

    def visit_set_session(self, node, context):
        return self.visit_statement(node, context)

    def visit_generic_literal(self, node, context):
        return self.visit_literal(node, context)

    def visit_time_literal(self, node, context):
        return self.visit_literal(node, context)

    def visit_explain_option(self, node, context):
        return self.visit_node(node, context)

    def visit_with(self, node, context):
        return self.visit_node(node, context)

    def visit_approximate(self, node, context):
        return self.visit_node(node, context)

    def visit_with_query(self, node, context):
        return self.visit_node(node, context)

    def visit_select(self, node, context):
        return self.visit_node(node, context)

    def visit_relation(self, node, context):
        return self.visit_node(node, context)

    def visit_query_body(self, node, context):
        return self.visit_relation(node, context)

    def visit_query_specification(self, node, context):
        return self.visit_query_body(node, context)

    def visit_set_operation(self, node, context):
        return self.visit_query_body(node, context)

    def visit_union(self, node, context):
        return self.visit_set_operation(node, context)

    def visit_intersect(self, node, context):
        return self.visit_set_operation(node, context)

    def visit_except(self, node, context):
        return self.visit_set_operation(node, context)

    def visit_timestamp_literal(self, node, context):
        return self.visit_literal(node, context)

    def visit_when_clause(self, node, context):
        return self.visit_expression(node, context)

    def visit_interval_literal(self, node, context):
        return self.visit_literal(node, context)

    def visit_in_predicate(self, node, context):
        return self.visit_expression(node, context)

    def visit_function_call(self, node, context):
        return self.visit_expression(node, context)

    def visit_lambda_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_simple_case_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_string_literal(self, node, context):
        return self.visit_literal(node, context)

    def visit_binary_literal(self, node, context):
        return self.visit_literal(node, context)

    def visit_boolean_literal(self, node, context):
        return self.visit_literal(node, context)

    def visit_in_list_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_qualified_name_reference(self, node, context):
        return self.visit_expression(node, context)

    def visit_dereference_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_null_if_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_if_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_null_literal(self, node, context):
        return self.visit_literal(node, context)

    def visit_arithmetic_unary(self, node, context):
        return self.visit_expression(node, context)

    def visit_not_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_select_item(self, node, context):
        return self.visit_node(node, context)

    def visit_single_column(self, node, context):
        return self.visit_select_item(node, context)

    def visit_all_columns(self, node, context):
        return self.visit_select_item(node, context)

    def visit_searched_case_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_like_predicate(self, node, context):
        return self.visit_expression(node, context)

    def visit_is_not_null_predicate(self, node, context):
        return self.visit_expression(node, context)

    def visit_is_null_predicate(self, node, context):
        return self.visit_expression(node, context)

    def visit_array_constructor(self, node, context):
        return self.visit_expression(node, context)

    def visit_subscript_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_long_literal(self, node, context):
        return self.visit_literal(node, context)

    def visit_logical_binary_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_subquery_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_sort_item(self, node, context):
        return self.visit_node(node, context)

    def visit_table(self, node, context):
        return self.visit_query_body(node, context)

    def visit_unnest(self, node, context):
        return self.visit_relation(node, context)

    def visit_values(self, node, context):
        return self.visit_query_body(node, context)

    def visit_row(self, node, context):
        return self.visit_node(node, context)

    def visit_table_subquery(self, node, context):
        return self.visit_query_body(node, context)

    def visit_aliased_relation(self, node, context):
        return self.visit_relation(node, context)

    def visit_sampled_relation(self, node, context):
        return self.visit_relation(node, context)

    def visit_join(self, node, context):
        return self.visit_relation(node, context)

    def visit_exists(self, node, context):
        return self.visit_expression(node, context)

    def visit_try_expression(self, node, context):
        return self.visit_expression(node, context)

    def visit_cast(self, node, context):
        return self.visit_expression(node, context)

    def visit_input_reference(self, node, context):
        return self.visit_expression(node, context)

    def visit_window(self, node, context):
        return self.visit_node(node, context)

    def visit_window_frame(self, node, context):
        return self.visit_node(node, context)

    def visit_frame_bound(self, node, context):
        return self.visit_node(node, context)

    def visit_call_argument(self, node, context):
        return self.visit_node(node, context)

    def visit_table_element(self, node, context):
        return self.visit_node(node, context)

    def visit_create_table(self, node, context):
        return self.visit_statement(node, context)

    def visit_create_table_as_select(self, node, context):
        return self.visit_statement(node, context)

    def visit_drop_table(self, node, context):
        return self.visit_statement(node, context)

    def visit_rename_table(self, node, context):
        return self.visit_statement(node, context)

    def visit_rename_column(self, node, context):
        return self.visit_statement(node, context)

    def visit_add_column(self, node, context):
        return self.visit_statement(node, context)

    def visit_create_view(self, node, context):
        return self.visit_statement(node, context)

    def visit_drop_view(self, node, context):
        return self.visit_statement(node, context)

    def visit_insert(self, node, context):
        return self.visit_node(node, context)

    def visit_call(self, node, context):
        return self.visit_node(node, context)

    def visit_delete(self, node, context):
        return self.visit_statement(node, context)

    def visit_start_transaction(self, node, context):
        return self.visit_statement(node, context)

    def visit_grant(self, node, context):
        return self.visit_statement(node, context)

    def visit_transaction_mode(self, node, context):
        return self.visit_node(node, context)

    def visit_isolation_level(self, node, context):
        return self.visit_transaction_mode(node, context)

    def visit_transaction_access_mode(self, node, context):
        return self.visit_transaction_mode(node, context)

    def visit_commit(self, node, context):
        return self.visit_statement(node, context)

    def visit_rollback(self, node, context):
        return self.visit_statement(node, context)

    def visit_at_time_zone(self, node, context):
        return self.visit_expression(node, context)


class DefaultTraversalVisitor(AstVisitor):
    def __init__(self, line=None, pos=None):
        super(DefaultTraversalVisitor, self).__init__(line, pos)

    def visit_extract(self, node, context):
        return self.process(node.expression, context)

    def visit_cast(self, node, context):
        return self.process(node.expression, context)

    def visit_arithmetic_binary(self, node, context):
        self.process(node.left, context)
        self.process(node.right, context)
        return None

    def visit_between_predicate(self, node, context):
        self.process(node.value, context)
        self.process(node.min, context)
        self.process(node.max, context)
        return None

    def visit_coalesce_expression(self, node, context):
        for operand in node.operands:
            self.process(operand, context)
        return None

    def visit_at_time_zone(self, node, context):
        self.process(node.value, context)
        self.process(node.time_zone, context)
        return None

    def visit_array_constructor(self, node, context):
        for expression in node.values:
            self.process(expression, context)
        return None

    def visit_subscript_expression(self, node, context):
        self.process(node.base, context)
        self.process(node.index, context)
        return None

    def visit_comparison_expression(self, node, context):
        self.process(node.left, context)
        self.process(node.right, context)
        return None

    def visit_query(self, node, context):
        self.process(node.query_body, context)
        for sort_item in node.order_by:
            self.process(sort_item, context)
        return None

    def visit_with(self, node, context):
        for query in node.queries:
            self.process(query, context)
        return None

    def visit_with_query(self, node, context):
        return self.process(node.query, context)

    def visit_select(self, node, context):
        for item in node.select_items:
            self.process(item, context)
        return None

    def visit_single_column(self, node, context):
        self.process(node.expression, context)
        return None

    def visit_when_clause(self, node, context):
        self.process(node.operand, context)
        self.process(node.result, context)
        return None

    def visit_in_predicate(self, node, context):
        self.process(node.value, context)
        self.process(node.value_list, context)
        return None

    def visit_function_call(self, node, context):
        for argument in node.arguments:
            self.process(argument, context)
        if node.window:
            self.process(node.window, context)
        return None

    def visit_dereference_expression(self, node, context):
        self.process(node.base, context)
        return None

    """
        def visit_window(self, node, context)
            for expression in node.partition:
                self.process(expression, context)
            for sort_item in node.order_by:
                self.process(sort_item.sort_key, context)
            if node.frame:
                self.process(node.frame, context)
            return None

        def visit_window_frame(self, node, context)
            self.process(node.start, context)
            if node.end:
                self.process(node.end, context)
            return None

        def visit_frame_bound(self, node, context)
            if node.value:
                self.process(node.value, context)
            return None
    """

    def visit_simple_case_expression(self, node, context):
        self.process(node.operand, context)
        for clause in node.when_clauses:
            self.process(clause, context)
        if node.default_value:
            self.process(node.default_valuee, context)
        return None

    def visit_in_list_expression(self, node, context):
        for value in node.values:
            self.process(value, context)
        return None

    def visit_None_if_expression(self, node, context):
        self.process(node.first, context)
        self.process(node.second, context)
        return None

    def visit_if_expression(self, node, context):
        self.process(node.condition, context)
        self.process(node.true_value, context)
        if node.false_value:
            self.process(node.false_value, context)
        return None

    def visit_try_expression(self, node, context):
        self.process(node.inner_expression, context)
        return None

    def visit_arithmetic_unary(self, node, context):
        return self.process(node.value, context)

    def visit_not_expression(self, node, context):
        return self.process(node.value, context)

    def visit_searched_case_expression(self, node, context):
        for clause in node.when_clauses:
            self.process(clause, context)
        if node.default_value:
            self.process(node.default_value, context)
        return None

    def visit_like_predicate(self, node, context):
        self.process(node.value, context)
        self.process(node.pattern, context)
        if node.escape is not None:
            self.process(node.escape, context)
        return None

    def visit_is_not_None_predicate(self, node, context):
        return self.process(node.value, context)

    def visit_is_None_predicate(self, node, context):
        return self.process(node.value, context)

    def visit_logical_binary_expression(self, node, context):
        self.process(node.left, context)
        self.process(node.right, context)
        return None

    def visit_subquery_expression(self, node, context):
        return self.process(node.query, context)

    def visit_sort_item(self, node, context):
        return self.process(node.sort_key, context)

    def visit_query_specification(self, node, context):
        self.process(node.select, context)
        if node.from_:
            self.process(node.from_, context)
        if node.where:
            self.process(node.where, context)
        if node.group_by:
            for grouping_element in node.group_by.grouping_elements:
                self.process(grouping_element, context)
        if node.having:
            self.process(node.having, context)
        for sort_item in node.order_by:
            self.process(sort_item, context)
        return None

    def visit_union(self, node, context):
        for relation in node.relations:
            self.process(relation, context)
        return None

    def visit_intersect(self, node, context):
        for relation in node.relations:
            self.process(relation, context)
        return None

    def visit_except(self, node, context):
        self.process(node.left, context)
        self.process(node.right, context)
        return None

    def visit_values(self, node, context):
        for row in node.rows:
            self.process(row, context)
        return None

    def visit_row(self, node, context):
        for expression in node.items:
            self.process(expression, context)
        return None

    def visit_table_subquery(self, node, context):
        return self.process(node.query, context)

    def visit_aliased_relation(self, node, context):
        return self.process(node.relation, context)

    def visit_sampled_relation(self, node, context):
        self.process(node.relation, context)
        self.process(node.get_sample_percentage(), context)
        if node.get_columns_to_stratify_on().is_present():
            for expression in node.get_columns_to_stratify_on().get():
                self.process(expression, context)
        return None

    def visit_join(self, node, context):
        self.process(node.left, context)
        self.process(node.right, context)
        join_on = [criteria for criteria in node.criter if isinstance(criteria, JoinOn)]
        for criteria in join_on:
            self.process(criteria.expression, context)

        return None


class DefaultExpressionTraversalVisitor(DefaultTraversalVisitor):
    def __init__(self, line=None, pos=None):
        super(DefaultExpressionTraversalVisitor, self).__init__(line, pos)

    def visit_subquery_expression(self, node, context):
        return None
