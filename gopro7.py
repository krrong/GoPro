from goprocam import GoProCamera, constants
import shutil

def takePhotoTransferDelete():
    go_pro.take_photo(timer=5)    # 5초 타이머를 두고 사진을 찍음
    go_pro.downloadLastMedia(custom_filename="selfies.jpg") # 마지막 미디어를 custom_filename으로 하여 다운로드
    # go_pro.delete("last")   # 마지막 미디어 삭제

def mediaDownload():
    medias = go_pro.downloadAll()

    # 다운받은 파일 위치 변경
    for media in medias:
        shutil.move('./100GOPRO-{}'.format(media), './images/100GOPRO{}'.format(media))

if __name__ == "__main__":
    go_pro = GoProCamera.GoPro()    # 고프로 객체 생성

    # go_pro.listMedia(True)  # 고프로 저장소에 저장된 내용을 보여줌
    # go_pro.delete("all")  # 고프로 저장소 모든 내용 삭제

    # go_pro.video_settings(res="1080p", fps="30")    # 고프로 비디오 세팅

    # go_pro.shoot_video()  # duration 만큼 동영상 촬영
    mediaDownload()
