import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""import lineapy

from PIL.Image import open, new

new_img = new("RGB", (4,4))
new_img.save("test.png", "PNG")
e = open("test.png")

lineapy.save(e, "testme")
""",
    location=PosixPath("[source file path]"),
)
import_1 = ImportNode(
    source_location=SourceLocation(
        lineno=3,
        col_offset=0,
        end_lineno=3,
        end_col_offset=31,
        source_code=source_1.id,
    ),
    library=Library(
        name="PIL.Image",
    ),
)
call_6 = CallNode(
    source_location=SourceLocation(
        lineno=6,
        col_offset=0,
        end_lineno=6,
        end_col_offset=31,
        source_code=source_1.id,
    ),
    function_id=CallNode(
        source_location=SourceLocation(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=12,
            source_code=source_1.id,
        ),
        function_id=LookupNode(
            name="getattr",
        ).id,
        positional_args=[
            CallNode(
                source_location=SourceLocation(
                    lineno=5,
                    col_offset=10,
                    end_lineno=5,
                    end_col_offset=27,
                    source_code=source_1.id,
                ),
                function_id=CallNode(
                    function_id=LookupNode(
                        name="getattr",
                    ).id,
                    positional_args=[
                        import_1.id,
                        LiteralNode(
                            value="new",
                        ).id,
                    ],
                ).id,
                positional_args=[
                    LiteralNode(
                        source_location=SourceLocation(
                            lineno=5,
                            col_offset=14,
                            end_lineno=5,
                            end_col_offset=19,
                            source_code=source_1.id,
                        ),
                        value="RGB",
                    ).id,
                    CallNode(
                        source_location=SourceLocation(
                            lineno=5,
                            col_offset=21,
                            end_lineno=5,
                            end_col_offset=26,
                            source_code=source_1.id,
                        ),
                        function_id=LookupNode(
                            name="l_tuple",
                        ).id,
                        positional_args=[
                            LiteralNode(
                                source_location=SourceLocation(
                                    lineno=5,
                                    col_offset=22,
                                    end_lineno=5,
                                    end_col_offset=23,
                                    source_code=source_1.id,
                                ),
                                value=4,
                            ).id,
                            LiteralNode(
                                source_location=SourceLocation(
                                    lineno=5,
                                    col_offset=24,
                                    end_lineno=5,
                                    end_col_offset=25,
                                    source_code=source_1.id,
                                ),
                                value=4,
                            ).id,
                        ],
                    ).id,
                ],
            ).id,
            LiteralNode(
                value="save",
            ).id,
        ],
    ).id,
    positional_args=[
        LiteralNode(
            source_location=SourceLocation(
                lineno=6,
                col_offset=13,
                end_lineno=6,
                end_col_offset=23,
                source_code=source_1.id,
            ),
            value="test.png",
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=6,
                col_offset=25,
                end_lineno=6,
                end_col_offset=30,
                source_code=source_1.id,
            ),
            value="PNG",
        ).id,
    ],
)
call_7 = CallNode(
    source_location=SourceLocation(
        lineno=7,
        col_offset=4,
        end_lineno=7,
        end_col_offset=20,
        source_code=source_1.id,
    ),
    function_id=CallNode(
        function_id=LookupNode(
            name="getattr",
        ).id,
        positional_args=[
            import_1.id,
            LiteralNode(
                value="open",
            ).id,
        ],
    ).id,
    positional_args=[
        LiteralNode(
            source_location=SourceLocation(
                lineno=7,
                col_offset=9,
                end_lineno=7,
                end_col_offset=19,
                source_code=source_1.id,
            ),
            value="test.png",
        ).id
    ],
)
