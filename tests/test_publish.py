"""
'linton publish' tests.
Copyright (c) Reuben Thomas 2024.
Released under the GPL version 3, or (at your option) any later version.
"""

from pathlib import Path
from typing import List, Callable

from pytest import CaptureFixture

from testutils import dir_test, make_tests, Case
from linton import main

test_files_dir = Path(__file__).parent.resolve() / "test-files"

pytestmark = make_tests(
    main,
    test_files_dir,
    Case(
        "from-init",
        ["publish", str(test_files_dir / "publish/from-init/input")],
    ),
)


# pylint: disable=similarities
def test_publish(
    function: Callable[[List[str]], None],
    case: Case,
    fixture_dir: Path,
    capsys: CaptureFixture[str],
    regenerate_expected: bool,
) -> None:
    dir_test(
        function,
        case,
        fixture_dir,
        capsys,
        regenerate_expected,
    )