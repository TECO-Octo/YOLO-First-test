import os
import glob


def prepare_files_for_conversion(base_dir, output_dir, ask_overwrite):
    """
    Discovers .avi files in the given base directory, prepares them for conversion,
    and asks the user for overwrite permissions if necessary.

    Parameters:
    - base_dir: The base directory to search for .avi files.
    - output_dir: The directory where converted files will be saved.
    - ask_overwrite: Asks the user whether to overwrite existing files.

    Returns:
    - A list of tuples, each containing the input path and output path for files ready for conversion.
    """
    files_to_convert = []

    # Discover directories matching 'predict*' pattern
    predict_dirs = glob.glob(os.path.join(base_dir, 'predict*'))

    for directory in predict_dirs:
        avi_files = [f for f in os.listdir(directory) if f.endswith('.avi')]

        for avi_file in avi_files:
            input_path = os.path.join(directory, avi_file)
            output_filename = os.path.splitext(avi_file)[0] + '.mp4'
            output_path = os.path.join(output_dir, output_filename)

            # Check if the output file already exists
            if os.path.exists(output_path) and not ask_overwrite(output_path):
                print("Skipping conversion for", avi_file)
                continue

            files_to_convert.append((input_path, output_path))
            print(files_to_convert)

    return files_to_convert
