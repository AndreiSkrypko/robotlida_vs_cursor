#!/usr/bin/env python3
"""
Автоматический скрипт для очистки проекта от ненужных файлов
"""

import os
import shutil
import glob

def cleanup_old_images():
    """Удаляет старые неоптимизированные изображения"""
    
    print("Cleaning up old unoptimized images...")
    print("-" * 40)
    
    # Директории со старыми изображениями
    old_dirs = [
        "main_app/static/main/img/fotocarusel",
        "static/main/img/fotocarusel",
        "main_app/static/main/img/about",
        "static/main/img/about",
        "main_app/static/main/img/courses",
        "static/main/img/courses",
        "main_app/static/main/img/index",
        "static/main/img/index"
    ]
    
    total_freed = 0
    total_files = 0
    
    for dir_path in old_dirs:
        if os.path.exists(dir_path):
            # Подсчитываем размер и количество файлов
            dir_size = 0
            file_count = 0
            
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                        file_path = os.path.join(root, file)
                        dir_size += os.path.getsize(file_path)
                        file_count += 1
            
            if file_count > 0:
                print(f"Removing {dir_path}: {file_count} files, {dir_size / 1024 / 1024:.1f} MB")
                shutil.rmtree(dir_path)
                total_freed += dir_size
                total_files += file_count
            else:
                print(f"Directory {dir_path} is empty, removing...")
                shutil.rmtree(dir_path)
    
    print(f"Total freed: {total_files} files, {total_freed / 1024 / 1024:.1f} MB")
    return True

def cleanup_scripts():
    """Удаляет временные скрипты оптимизации"""
    
    print("\nCleaning up optimization scripts...")
    print("-" * 40)
    
    # Скрипты для удаления
    scripts_to_remove = [
        "optimize_images.py",
        "update_image_paths.py", 
        "optimize_all_images.py",
        "update_all_image_paths.py",
        "cleanup_old_images.py",
        "simple_cleanup.py",
        "auto_cleanup.py"
    ]
    
    removed_count = 0
    for script in scripts_to_remove:
        if os.path.exists(script):
            print(f"Removing {script}")
            os.remove(script)
            removed_count += 1
    
    print(f"Removed {removed_count} scripts")
    return True

def cleanup_documentation():
    """Удаляет временную документацию"""
    
    print("\nCleaning up documentation files...")
    print("-" * 40)
    
    # Документация для удаления
    docs_to_remove = [
        "GALLERY_OPTIMIZATION_GUIDE.md",
        "IMPLEMENTATION_GUIDE.md",
        "TESTING_INSTRUCTIONS.md",
        "FINAL_TESTING_GUIDE.md",
        "GALLERY_FIX_GUIDE.md"
    ]
    
    removed_count = 0
    for doc in docs_to_remove:
        if os.path.exists(doc):
            print(f"Removing {doc}")
            os.remove(doc)
            removed_count += 1
    
    print(f"Removed {removed_count} documentation files")
    return True

def cleanup_backup_files():
    """Удаляет резервные копии HTML файлов"""
    
    print("\nCleaning up backup files...")
    print("-" * 40)
    
    # Находим все .backup файлы
    backup_files = glob.glob("main_app/templates/**/*.backup", recursive=True)
    
    removed_count = 0
    for backup_file in backup_files:
        print(f"Removing {backup_file}")
        os.remove(backup_file)
        removed_count += 1
    
    print(f"Removed {removed_count} backup files")
    return True

def cleanup_duplicate_images():
    """Удаляет дублирующиеся оптимизированные изображения"""
    
    print("\nCleaning up duplicate optimized images...")
    print("-" * 40)
    
    # Директории с оптимизированными изображениями
    optimized_dirs = [
        "main_app/static/main/img/fotocarusel_optimized",
        "main_app/static/main/img/about_optimized",
        "main_app/static/main/img/courses_optimized", 
        "main_app/static/main/img/index_optimized"
    ]
    
    total_freed = 0
    total_files = 0
    
    for dir_path in optimized_dirs:
        if os.path.exists(dir_path):
            # Удаляем JPEG fallback файлы, оставляем только WebP
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    if file.endswith('_optimized.jpg'):
                        file_path = os.path.join(root, file)
                        file_size = os.path.getsize(file_path)
                        print(f"Removing {file_path}")
                        os.remove(file_path)
                        total_freed += file_size
                        total_files += 1
    
    print(f"Removed {total_files} JPEG fallback files, freed {total_freed / 1024 / 1024:.1f} MB")
    return True

def cleanup_empty_directories():
    """Удаляет пустые директории"""
    
    print("\nCleaning up empty directories...")
    print("-" * 40)
    
    # Находим пустые директории
    empty_dirs = []
    
    for root, dirs, files in os.walk("main_app/static", topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):  # Директория пустая
                empty_dirs.append(dir_path)
    
    removed_count = 0
    for empty_dir in empty_dirs:
        print(f"Removing empty directory: {empty_dir}")
        os.rmdir(empty_dir)
        removed_count += 1
    
    print(f"Removed {removed_count} empty directories")
    return True

def main():
    """Основная функция очистки"""
    
    print("Automatic Project Cleanup")
    print("Removing old images, scripts, and documentation")
    print("=" * 50)
    
    # Выполняем очистку
    cleanup_old_images()
    cleanup_scripts()
    cleanup_documentation()
    cleanup_backup_files()
    cleanup_duplicate_images()
    cleanup_empty_directories()
    
    print("\n" + "=" * 50)
    print("CLEANUP COMPLETED!")
    print("=" * 50)
    
    print("\nRemaining files:")
    print("- Optimized WebP images in *_optimized directories")
    print("- COMPLETE_OPTIMIZATION_REPORT.md (final report)")
    print("- All HTML templates with updated paths")
    print("- Django project files")
    
    print("\nNext steps:")
    print("1. Test your website to ensure everything works")
    print("2. Run collectstatic to update static files")
    print("3. Deploy to production server")

if __name__ == "__main__":
    main()
