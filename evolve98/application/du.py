import os
def du():
    try:
        directory_path = input("Dizin: ")

        def get_directory_size(directory_path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(directory_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(file_path)
            return total_size

        def format_size(size_in_bytes):
            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if size_in_bytes < 1024.0:
                    return "{:.2f} {}".format(size_in_bytes, unit)
                size_in_bytes /= 1024.0
            # Büyük boyutlar için döngüden çıkıldığında bir değer döndür
            return "{:.2f} TB".format(size_in_bytes)

        directory_size = get_directory_size(directory_path)

        print("\nDizin Boyutu:", format_size(directory_size))

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
