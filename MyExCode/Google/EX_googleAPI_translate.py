from google.cloud import translate


# google API 翻譯 範例(要錢)
def google_translate_text(project_id, source_language_code, target_language_code, text):
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": source_language_code,
            "target_language_code": target_language_code,
        }
    )

    result = []
    for translation in response.translations:
        result.append(translation.translated_text)

    return result


print(google_translate_text('dgcmtcloud043', 'th', 'en', 'สวัสดี'))
