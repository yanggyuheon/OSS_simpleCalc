import logging

def make_logger(name=None):
    # filemode = append로 기존 파일에 이어서 기록
    logging.basicConfig(filemode='a')

    # logger instance 생성
    logger = logging.getLogger(name)

    # logger의 level을 가장 낮은 수준인 DEBUG로 설정
    logger.setLevel(logging.DEBUG)

    # error/normal 나누기
    if name == "error":
        # formatter 지정
        formatter = logging.Formatter("%(asctime)s  %(message)s")
        
        # handler instance 생성
        file_handler = logging.FileHandler(filename="error.log")

    elif name == "normal":
        # formatter 지정
        formatter = logging.Formatter("%(asctime)s  %(message)s")
        
        # handler instance 생성
        file_handler = logging.FileHandler(filename="normal.log")

    else: # error/normal 이외 종료처리
        exit(1)

    
    # handler level 설정 : 예상대로 작동하는지에 대한 확인 수준이므로 INFO로 설정
    file_handler.setLevel(logging.INFO)

    #6 handler 출력 format 지정
    file_handler.setFormatter(formatter)

    #7 logger에 handler 추가
    logger.addHandler(file_handler)

    return logger