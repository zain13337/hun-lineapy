import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="a = min(abs(11), 10)",
    working_directory="dummy_linea_repo/",
    libraries=[],
)
variable_1 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=1,
        col_offset=0,
        end_lineno=1,
        end_col_offset=20,
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=1,
                    col_offset=8,
                    end_lineno=1,
                    end_col_offset=15,
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                lineno=1,
                                col_offset=12,
                                end_lineno=1,
                                end_col_offset=14,
                                value=11,
                            ).id,
                        ).id
                    ],
                    function_id=LookupNode(
                        id=get_new_id(),
                        session_id=session.id,
                        name="abs",
                    ).id,
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=1,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=1,
                    col_offset=17,
                    end_lineno=1,
                    end_col_offset=19,
                    value=10,
                ).id,
            ).id,
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="min",
        ).id,
    ).id,
    assigned_variable_name="a",
)