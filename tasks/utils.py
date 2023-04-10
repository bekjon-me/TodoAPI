# Utils
from django.contrib.contenttypes.models import ContentType
from django.http import FileResponse


def cal_key(obj, m, content_type_=False, object_id_=False):
    present_keys = False
    if m.__name__ == "Task":
        present_keys = (
            m.objects.filter(project=obj)
            .order_by("-ptid")
            .values_list("ptid", flat=True)
        )
    elif m.__name__ == "SubTask":
        present_keys = (
            m.objects.filter(task=obj).order_by("-tsid").values_list("tsid", flat=True)
        )
    elif m.__name__ == "AttachedFile":
        content_type__ = ContentType.objects.get(
            app_label=content_type_.app_label, model=content_type_.model
        )
        present_keys = (
            m.objects.filter(content_type=content_type__.id, object_id=object_id_)
            .order_by("-tfid")
            .values_list("tfid", flat=True)
        )

    if present_keys:
        return present_keys[0] + 1
    else:
        return 1


from django.http import FileResponse


def download_file(request, filefield):
    # Open the file
    with filefield.open() as file:
        # Read the file content
        file_content = file.read()

        # Get the range from the headers
        range_header = request.META.get("HTTP_RANGE")
        if range_header is None:
            # If no range is provided, send the entire file
            response = FileResponse(file, filename=filefield.path)
        else:
            # If a range is provided, send the specified range
            start_range, end_range = range_header.split("=")[1].split("-")
            start_range = int(start_range)
            end_range = int(end_range) if end_range else len(file_content) - 1
            content_range = f"bytes {start_range}-{end_range}/{len(file_content)}"
            response = FileResponse(
                file_content[start_range : end_range + 1],
                content_type="application/octet-stream",
                filename=filefield.path,
            )
            response["Content-Range"] = content_range

        # Set the content length header
        # response["Content-Length"] = str(len(file_content))

    # Set the content disposition header
    response["Content-Disposition"] = f'attachment; filename="{filefield.name}"'

    return response
