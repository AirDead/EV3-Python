from lib import ColorLogger

if __name__ == "__main__":
    logger = ColorLogger()
    logger.load_all_cogs('cogs')  # Загрузка всех когов из папки 'cogs'
    
    while True:
        logger.check_color()
