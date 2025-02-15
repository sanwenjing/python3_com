import os
import subprocess
import shutil
import sys
import logging

# 设置日志配置
logging.basicConfig(filename='video_compression.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def compress_video(input_path, output_path):
    try:
        # 使用ffmpeg压缩视频到1K分辨率
        command = [
            'ffmpeg.exe', '-i', input_path, '-vf', 'scale=1024:-1', '-c:a', 'copy', output_path
        ]
        subprocess.run(command, check=True)
        logging.info(f"Successfully compressed {input_path} to {output_path}")
    except subprocess.CalledProcessError as e:
        # 如果压缩失败，直接拷贝文件
        shutil.copy2(input_path, output_path)
        logging.warning(f"Failed to compress {input_path}, copied instead. Error: {e}")

def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        # 创建对应的输出目录
        relative_path = os.path.relpath(root, input_dir)
        current_output_dir = os.path.join(output_dir, relative_path)
        os.makedirs(current_output_dir, exist_ok=True)

        for file in files:
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(current_output_dir, file)

            # 只处理视频文件
            if file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                compress_video(input_file_path, output_file_path)
            else:
                # 非视频文件直接拷贝
                shutil.copy2(input_file_path, output_file_path)
                logging.info(f"Copied non-video file {input_file_path} to {output_file_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python compress_videos.py <input_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = os.path.join(os.path.dirname(input_directory), 'CompressedVideos')

    # 创建输出目录
    os.makedirs(output_directory, exist_ok=True)

    # 处理目录
    process_directory(input_directory, output_directory)
    logging.info("Video compression process completed.")

if __name__ == "__main__":
    main()