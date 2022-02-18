def item_cleaner(items):
    out = []
    for i in items:
        el = i.name
        id_ = i.get('id')
        id_ = id_.strip() if id_ is not None else ""
        class_ = i.get('class')
        if class_ is None:
            class_ = ""
        text = i.text
        text = text.strip() if text is not None else ""
        href = i.get('href')
        href = href.strip() if href is not None else ""
        src = i.get('src')
        if src is None:
            src = ""
        alt = i.get('alt')
        alt = alt.strip() if alt is not None else ""
        content = i.get('content')
        content = content.strip() if content is not None else ""
        name = i.get('name')
        name = name.strip() if name is not None else ""

        out.append(
            {"el": el, "id": id_, "class": class_, "text": text, "href": href, "src": src, "alt": alt,
             "content": content, "name": name})
    return out