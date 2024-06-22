import reflex as rx


def profile_image():
    return rx.box(
        rx.image(
            src="profile.jpeg",
            alt="Profile photo of John Doe",
            height="12rem",
            object_fit="cover",
            width="12rem",
        ),
        border_radius="9999px",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        border_width="4px",
        border_color=rx.color("gray", 1),
        overflow="hidden",
    )


def profile_info():
    return rx.vstack(
        rx.heading(
            "Nikhil Rao", 
            font_size="1.5rem",
            line_height="2rem",
            font_weight="600",
        ),
        rx.markdown(
            """👋 Welcome to my page!

I'm building [Reflex](https://reflex.dev) - an [open source](https://github.com/reflex-dev/reflex) framework to build web apps with Python and generative AI.

If you're interested in web development, AI, or just want to chat, feel free to [reach out](mailto:nikhil@reflex.dev). We're hiring too! 🚀
            """,
            margin_bottom="1.5rem",
        ),
        rx.hstack(
            social_links(),
            contact_button(),
            align="center",
            spacing="7"
        ),
        style={"@media (min-width: 768px)": {"width": "66.666667%"}},
        padding="2rem",
        background_color=rx.color("accent", 1),
    )


def social_links():
    return rx.hstack(
        social_icon("twitter", "https://twitter.com/nikhi1rao"),
        social_icon("github", "https://github.com/picklelo"),
        social_icon("linkedin", "https://linkedin.com/in/nrao95"),
        spacing="4",
    )


def social_icon(icon, link):
    return rx.link(
        rx.icon(
            icon,
            # color=rx.color("accent", 9),
            # _hover={"color": rx.color("acce", 10)}
        ),
        href=link,
    )


def contact_button():
    return rx.button(
        "Get in touch", 
        size="4",
        variant="outline",
        border_radius="0.25rem",
    )


def badge():
    return rx.fragment(
        rx.flex(
            rx.flex(
                profile_image(),
                align_items="center",
                style={"@media (min-width: 768px)": {"width": "33.333333%"}},
                display="flex",
                justify_content="center",
                padding="2rem",
                background_color=rx.color("accent", 2),
            ),
            profile_info(),
            background_color=rx.color("accent", 1),
            flex_direction="column",
            display="flex",
            max_width="56rem",
            border_radius="0.5rem",
            overflow="hidden",
            width="100%",
            style={"@media (min-width: 768px)": {"flex-direction": "row"}},
            box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
        ),
    )
