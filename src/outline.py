"""Generate the fabrication outline for the revision 3 sensor board."""

BOARD_WIDTH_MM = 68.0
BOARD_HEIGHT_MM = 41.5
CORNER_RADIUS_MM = 3.0
MOUNT_HOLE_MM = 3.2


def corners():
    """Return the four mounting-hole centres in board coordinates."""
    inset = MOUNT_HOLE_MM + 2.0
    return [
        (inset, inset),
        (BOARD_WIDTH_MM - inset, inset),
        (inset, BOARD_HEIGHT_MM - inset),
        (BOARD_WIDTH_MM - inset, BOARD_HEIGHT_MM - inset),
    ]


def describe():
    return {
        "width_mm": BOARD_WIDTH_MM,
        "height_mm": BOARD_HEIGHT_MM,
        "corner_radius_mm": CORNER_RADIUS_MM,
        "mount_holes": corners(),
    }


if __name__ == "__main__":
    print(describe())
