from telegraph import Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name="AIBot")

def post_to_telegraph(title: str, content: str) -> str:
    response = telegraph.create_page(
        title=title[:50],
        html_content=content,
    )
    return f"https://telegra.ph/{response['path']}"
