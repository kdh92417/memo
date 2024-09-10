from django.db import models


# class UserCategory(models.Model):
#     pass


class UserMemo(models.Model):
    memo_content = models.TextField("메모", blank=True, null=True)
    category = models.CharField("카테고리", blank=True, null=True, max_length=100)
    user_id = models.CharField("유저ID", max_length=100)


# logo_image = models.ImageField(
#         "로고이미지", width_field="logo_image_width", height_field="logo_image_height", null=True, blank=True, storage=S3PublicMediaStorage
#     )
#     logo_image_width = models.IntegerField("로고이미지 너비", null=True, blank=True)
#     logo_image_height = models.IntegerField("로고이미지 높이", null=True, blank=True)
#     name = models.CharField("병원명", max_length=100)
#     description = models.TextField("병원 소개", null=True, blank=True)
#     one_line_description = models.CharField("병원 한줄 소개", max_length=300, null=True, blank=True)
#     address = models.TextField("주소", null=True, blank=True)
#     longitude = models.DecimalField("경도", max_digits=10, decimal_places=7, null=True, blank=True)
#     latitude = models.DecimalField("위도", max_digits=10, decimal_places=7, null=True, blank=True)
#     near_station_name = models.CharField("가까운 역", max_length=100, null=True, blank=True)
#     phone_number = models.CharField("병원 연락처", max_length=100, null=True, blank=True)
#     sms_phone_number = models.CharField("병원 SMS 수신 연락처", max_length=100, null=True, blank=True)