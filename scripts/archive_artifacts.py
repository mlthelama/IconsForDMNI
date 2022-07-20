import argparse
import os
import zipfile

def make_rel_archive(a_args):
    archive = zipfile.ZipFile(a_args.name + ".zip", "w", zipfile.ZIP_DEFLATED)
    archive.write(
        os.path.join(a_args.src_dir, "build", "avatars_for_dmni.swf"),
        "Interface/avatars_for_dmni.swf")


def parse_arguments():
    parser = argparse.ArgumentParser(description="archive build artifacts for distribution")
    parser.add_argument("--name", type=str, help="the project name", required=True)
    parser.add_argument("--src-dir", type=str, help="the project root source directory", required=True)
    return parser.parse_args()

def main():
    out = "artifacts"
    try:
        os.mkdir(out)
    except FileExistsError:
        pass
    os.chdir(out)

    args = parse_arguments()
    make_rel_archive(args)

if __name__ == "__main__":
	main()
