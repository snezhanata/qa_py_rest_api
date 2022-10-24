from voluptuous import Schema, PREVENT_EXTRA

post_create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

get_single_user_schema = Schema(
    {
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str,
        },
        "support": {
            "url": str,
            "text": str,
        },
    },
    required=True,
    extra=PREVENT_EXTRA,
)

post_login_successful = Schema(
    {"token": str},
    required=True,
    extra=PREVENT_EXTRA,
)

patch_update_job = Schema({"name": str, "job": str, "updatedAt": str})
