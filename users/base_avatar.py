import svgwrite


def get_basic_svg(username: str):
    filename = f"{username}_base"
    text = username[0].upper()
    dwg = svgwrite.Drawing(filename, size=("150px", "150px"))
    dwg.add(
        dwg.rect(
            insert=(0, 0), size=("150px", "150px"), rx=30.0, ry=30.0, fill="#e39e54"
        )
    )
    dwg.add(
        dwg.text(
            text,
            insert=(75.0, 93.0),
            fill="white",
            style="font-family: Roboto, sans-serif; font-size: 50.0px; text-anchor: middle;",
        )
    )
    path = f"users_base_svg/{filename}.svg"
    dwg.saveas(f"media/{path}")
    return path


# <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 150 150">
# <rect x="0" y="0" width="150" height="150" rx="30.0" ry="30.0" fill="#e39e54"/>
# <text text-anchor="middle" fill="white" x="75.0" y="93.0" style="font-family: Roboto, sans-serif; font-size: 50.0px; letter-spacing:0.05em">
#     КЗ
# </text></svg>
