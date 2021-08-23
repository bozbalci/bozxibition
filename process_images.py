import json
import os
import time

PDF_ROOT = "public/pictures/raw/"
OUTPUT_ROOT = "public/pictures/flat-processed/"
INDEX_PATH = "src/imageIndex.json"


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def extract_pdf_images():
    print(f"Extracting full resolution images from PDFs.")
    t_start = time.time()
    for root, dirs, files in os.walk(PDF_ROOT):
        if root == PDF_ROOT:
            continue

        collection_name = os.path.basename(os.path.normpath(root))

        for filename in files:
            real_name, ext = os.path.splitext(filename)

            if ext != ".pdf":
                continue

            print(f"Processing {collection_name}/{real_name}")
            input_filename = os.path.join(root, filename)
            output_prefix = os.path.join(OUTPUT_ROOT, f"{collection_name}-{real_name}")
            t0 = time.time()
            os.system(f"pdfimages -j {input_filename} {output_prefix}")
            t1 = time.time()
            print(f"Processed in {t1 - t0:.2f} seconds.")
    t_end = time.time()
    print(f"Extracted full resolution images from PDFs in {t_end - t_start} seconds.")


def generate_compressed_and_thumbs():
    """
    Can't be arsed to implement this rn, just the following commands:

        cd public/pictures
        mkdir flat-thumbnails
        mogrify -resize 10% -quality 85% -path flat-thumbnails flat-processed/*.jpg
    """


def generate_index():
    """
    {
        "macaasi": {
            "macaasi1": {
                "p": ["macaasi-macaasi1-000.jpg"],
                "m": "iback",
                "t": "04452
            }
        }
    }
    :return:
    """
    filenames = os.listdir(OUTPUT_ROOT)
    result = {}
    collections = set()

    for filename in sorted(filenames):
        real_name, ext = os.path.splitext(filename)
        collection, item, idx = real_name.split('-')
        collections.add(collection)

        if collection not in result:
            result[collection] = {}
        if item not in result[collection]:
            result[collection][item] = {}
        if 'p' not in result[collection][item]:
            result[collection][item]['p'] = []
        result[collection][item]['p'].append(filename)

    # Collect metadata
    for collection in collections:
        meta_path = os.path.join(PDF_ROOT, collection, "meta")
        if os.path.isfile(meta_path):
            with open(meta_path, 'r') as infile:
                meta_contents = infile.readlines()
            for line in meta_contents:
                item_with_colon, modifier = line.strip().split()
                item = item_with_colon[:-1]
                print(item, modifier)

                if 'm' not in result[collection][item]:
                    result[collection][item]['m'] = modifier

    with open(INDEX_PATH, 'w') as outfile:
        json.dump(result, outfile)


if __name__ == '__main__':
    # extract_pdf_images()
    generate_index()
