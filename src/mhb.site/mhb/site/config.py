# -*- coding: utf-8 -*-
"""Module providing widget setting constants"""
from adk.site import _

PKG_IMAGE_SCALES = ("ratio31", "collage")

PKG_WIDGETS = {
    "adk-page-section-header": {
        "pkg": "adk.site",
        "id": "adk-page-section-header",
        "name": "ADK Page Section Header",
        "title": "Page Section Header",
        "category": "more",
        "type": "content-item",
        "schema": "adk.site.widgets.content.interfaces.IADKWidgetPageSectionHeader",  # noqa
        "schemata": [],
        "node": {},
    },
    "adk-page-section": {
        "pkg": "adk.site",
        "id": "adk-page-section",
        "name": "ADK Page Section",
        "title": "ADK Page Section",
        "category": "more",
        "type": "content-item",
        "schema": "adk.site.widgets.content.interfaces.IADKWidgetPageSection",  # noqa
        "schemata": [],
        "node": {},
    },
    "adk-page-hero": {
        "pkg": "adk.site",
        "id": "adk-page-hero",
        "name": "ADK Page Hero",
        "title": "ADK Page Hero",
        "category": "more",
        "type": "content-item",
        "schema": "adk.site.widgets.content.interfaces.IADKWidgetPageHero",  # noqa
        "schemata": [],
        "node": {},
    },
    "adk-teaser-links": {
        "pkg": "adk.site",
        "id": "adk-teaser-links",
        "name": "ADK Teaser Links",
        "title": "ADK Teaser Links",
        "category": "more",
        "type": "collection",
        "schema": "adk.site.widgets.teaser.interfaces.IADKWidgetTeaserLinksInternal",  # noqa
        "schemata": [],
        "node": {
            "title": "Teaser Internal Link",
            "schema": "adk.site.widgets.teaser.interfaces.IADKWidgetLinkInternal",  # noqa
        },
    },
    "adk-collage": {
        "pkg": "adk.site",
        "id": "adk-collage",
        "name": "ADK Image Collage",
        "title": "ADK Image Collage",
        "category": "more",
        "type": "collection",
        "schema": "adk.site.widgets.gallery.collage.interfaces.IADKWidgetCollage",  # noqa
        "schemata": [],
        "node": {
            "title": "Teaser Internal Link",
            "schema": "adk.site.widgets.gallery.collage.interfaces.IADKWidgetCollageItem",  # noqa
        },
    },
}

BOOKING_FORM = {
    "personnel": {
        "legend": _("Personnel Information"),
        "fields": [
            {
                "field_type": "select",
                "field_id": "gender",
                "name": _("Gender"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": {
                    "female": _("Female"),
                    "male": _("Male"),
                    "other": _("Other"),
                },
            },
            {
                "field_type": "text-line",
                "field_id": "first_name",
                "name": _("First name"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "last_name",
                "name": _("Last name"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "street",
                "name": _("Street"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "postcode",
                "name": _("Postcode"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "city",
                "name": _("City"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "country",
                "name": _("Country"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "occupation",
                "name": _("Occupation"),
                "help_text": None,
                "required": False,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "phone",
                "name": _("Phone"),
                "help_text": None,
                "required": False,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "email",
                "name": _("Email"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "date_of_birth",
                "name": _("Date of Birth"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "nationality",
                "name": _("Nationality"),
                "help_text": None,
                "required": False,
                "class": "spacer",
                "options": None,
            },
        ],
    },
    "details": {
        "legend": _("Please specify your booking request"),
        "fields": [
            {
                "field_type": "select",
                "field_id": "course",
                "name": _("Herby, I register for following course"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": {
                    "intensive-course": _("Intensive Courses"),
                    "summer-course": _("Summer Courses for Teenagers"),
                },
            },
            {
                "field_type": "text-line",
                "field_id": "start",
                "name": _("Course stating date"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "course_duration",
                "name": _("Course duration in weeks"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "select",
                "field_id": "german_skills_level",
                "name": _("German language skills"),
                "help_text": None,
                "required": True,
                "class": "spacer",
                "options": {
                    "none": _("None"),
                    "elementary": _("Elementary"),
                    "intermediate": _("Intermediate"),
                    "good": _("Good"),
                    "advanced": _("Advanced"),
                },
            },
            {
                "field_type": "select",
                "field_id": "accommodation",
                "name": _("Preferred type of accommodation"),
                "help_text": None,
                "required": False,
                "class": "spacer",
                "options": {
                    "host-family-double-room-half-board": _(
                        "Host family, double room, half board"
                    ),
                    "host-family-double-room-full-board": _(
                        "host family, double room, full board"
                    ),
                    "host-family-single-room-half-board": _(
                        "Host family, single room, half board"
                    ),
                    "host-family-single-room-full-board": _(
                        "Host family, single room, full board"
                    ),
                    "no-accommodation-needed": _("No accommodation needed"),
                },
            },
            {
                "field_type": "text-line",
                "field_id": "arrival",
                "name": _("Day of arrival"),
                "help_text": _("Please use the format DD.MM.YYYY"),
                "required": True,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-line",
                "field_id": "departure",
                "name": _("Day of departure"),
                "help_text": _("Please use the format DD.MM.YYYY"),
                "required": False,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "boolean",
                "field_id": "airport-transfer",
                "name": _("Airport transfer"),
                "help_text": None,
                "required": False,
                "default": False,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "text-area",
                "field_id": "message",
                "name": _("Message"),
                "help_text": None,
                "required": False,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "boolean",
                "field_id": "privacy-policy",
                "name": _(
                    "By sending this message, I confirm that my details are "
                    "correct and I agree to the collection and further "
                    "processing of the provided data. The data will only be "
                    "used for the purpose stated in your inquiry."
                ),
                "help_text": None,
                "required": True,
                "default": False,
                "class": "spacer",
                "options": None,
            },
            {
                "field_type": "privacy",
                "field_id": "privacy-agreement",
                "name": _("Privacy Agreement"),
                "help_text": {
                    "help_text_prefix": _("I have acknowledged the "),
                    "help_text_link": _("privacy policy"),
                    "help_text_link_url": "/rechtliche-hinweise",
                    "help_text_postfix": _("and accept it."),
                },
                "required": True,
                "default": False,
                "class": "spacer",
                "options": None,
            },
        ],
    },
}
