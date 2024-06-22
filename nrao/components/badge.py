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
        rx.el.h1(
            "Nikhil Rao", 
            color=rx.color("gray", 12),
            font_size="1.5rem",
            line_height="2rem",
            font_weight="600",
            margin_bottom="0.5rem",
        ),
        rx.el.h2(
            "CEO at ", rx.link("Reflex", href="https://reflex.dev", is_external=True),
            color=rx.color("gray", 11),
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        rx.text(
            "Passionate about creating beautiful and functional web experiences. With over 5 years of experience in front-end development and UI/UX design, I bring ideas to life through clean code and intuitive interfaces.",
            color=rx.color("gray", 11),
            margin_bottom="1.5rem",
        ),
        social_links(),
        contact_button(),
        background_image="background-image",
        style={"@media (min-width: 768px)": {"width": "66.666667%"}},
        padding="2rem",
        background_color=rx.color("gray", 3),
    )


def social_links():
    return rx.flex(
        social_icon("twitter", "https://twitter.com/nikhi1rao"),
        social_icon("github", "https://github.com/picklelo"),
        social_icon("linkedin", "https://linkedin.com/in/nrao95"),
        column_gap="1rem",
        display="flex",
        margin_bottom="1.5rem",
    )


def social_icon(icon, link):
    return rx.link(
        rx.icon(
            icon,
        ),
        href=link,
        color=rx.color("gray", 8),
        _hover={"color": rx.color("gray", 10)}
    )


def contact_button():
    return rx.button(
        "Get in touch", 
        size="4",
        color_scheme="gray",
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
                background_color=rx.color("gray", 4),
            ),
            profile_info(),
            background_color=rx.color("gray", 1),
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
