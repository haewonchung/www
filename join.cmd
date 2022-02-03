@REM Off unnecessary Commands.
@echo off

chcp 65001 

set project_name= world wonder wine
@REM Server Information.
echo --------------------------------------------
echo.
echo 프로젝트 참가 인원 : 정혜원, 김미지, 유성훈, 조성현, 유민우 
echo 프로젝트 기한 일자 : 2022-01-26 ~ 2022-02-09
echo 프로젝트 이름 : %project_name%
echo mysql 버전 : 아직 안적음.
echo Django 버전 : 4.0.1
echo.
echo --------------------------------------------

@REM 폴더 최상위로 돌아가기.
echo 서버 실행 폴더 진입합니다...


echo %project_name% 서버에 진입합니다...
python manage.py runserver
