from typing import Sequence
from google.cloud import vision
import os

def analyze_image_from_uri(
    image_uri: str,
    feature_types: Sequence,
) -> vision.AnnotateImageResponse:
    client = vision.ImageAnnotatorClient()

    image = vision.Image()
    image.source.image_uri = image_uri
    features = [vision.Feature(type_=feature_type) for feature_type in feature_types]
    request = vision.AnnotateImageRequest(image=image, features=features)

    response = client.annotate_image(request=request)

    return response

def print_labels(response: vision.AnnotateImageResponse):
    print("=" * 80)
    for label in response.label_annotations:
        print(
            f"{label.score:4.0%}",
            f"{label.description:5}",
            sep=" | ",
        )

if __name__ == "__main__":
    image_uri = os.environ.get("IMAGE_URI")
    if not image_uri:
        print("Error: IMAGE_URI environment variable must be set.")
        exit(1)

    try:
        response = analyze_image_from_uri(
            image_uri=image_uri,
            feature_types=[vision.Feature.Type.LABEL_DETECTION]
        )
        print_labels(response)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)
