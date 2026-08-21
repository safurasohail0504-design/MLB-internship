from pathlib import Path
# File size limits
MAX_VIDEO_SIZE = 500 * 1024 * 1024  # 500 MB
MAX_IMAGE_SIZE = 50 * 1024 * 1024   # 50 MB
ALLOWED_VIDEO_EXTENSIONS = {
    ".mp4",
    ".avi",
    ".mov",
    ".mkv"
}
ALLOWED_IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif"
}
def is_allowed_video(filename: str) -> bool:
    """Check if file extension is allowed"""
    extension = Path(filename).suffix.lower()
    return extension in ALLOWED_VIDEO_EXTENSIONS
def is_allowed_image(filename: str) -> bool:
    """Check if file extension is allowed"""
    extension = Path(filename).suffix.lower()
    return extension in ALLOWED_IMAGE_EXTENSIONS
def get_file_size_mb(file_bytes: bytes) -> float:
    """Convert bytes to MB"""
    return len(file_bytes) / (1024 * 1024)
def validate_file_size(file_bytes: bytes, max_size: int, file_type: str) -> tuple:
    """
    Validate file size
    Returns: (is_valid, error_message)
    """
    size_mb = get_file_size_mb(file_bytes)
    max_size_mb = max_size / (1024 * 1024)
    if size_mb > max_size_mb:
        return False, f"{file_type} exceeds {max_size_mb}MB limit. Uploaded: {size_mb:.2f}MB"
    
    return True, None