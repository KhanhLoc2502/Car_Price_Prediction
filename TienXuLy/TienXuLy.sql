Select * from [dbo].[detail_oto]
Select * from [dbo].[Oto]

------------UPDATE detail_oto------------
UPDATE detail_oto
set [Năm_SX] = REPLACE([Năm_SX],N'Năm SX ',''),
[Kiểu_dáng]= REPLACE([Kiểu_dáng],N'Kiểu dáng ',''),
[Tình_trạng]= REPLACE([Tình_trạng],N'Tình trạng ',''),
[Xuất_xứ]= REPLACE([Xuất_xứ],N'Xuất xứ ',''),
[Tỉnh_thành] = REPLACE([Tỉnh_thành],N'Tỉnh thành',''),
[Quận_huyện]= REPLACE([Quận_huyện],N'Quận huyện',''),
[Hộp_số]= REPLACE([Hộp_số],N'Hộp số ',''),
[Nhiên_liệu]= REPLACE([Nhiên_liệu],N'Nhiên liệu ','')

UPDATE detail_oto
SET [Km_đã_đi]=0 where [Km_đã_đi] = 'None'

UPDATE detail_oto
SET [Km_đã_đi]=REPLACE(REPLACE([Km_đã_đi],N'Km đã đi ',''),' km','') where [Km_đã_đi] like N'%Km đã đi%'

--Thêm cột Hãng xe--
ALTER TABLE detail_oto
ADD [Hãng_xe] nvarchar(30)

UPDATE detail_oto
SET [Hãng_xe]= RTRIM(LTRIM(SUBSTRING([Tên_xe],1,CHARINDEX(' ', [Tên_xe]))))

Select * from detail_oto

------------UPDATE Oto------------
UPDATE Oto
SET [SĐT_người_bán]= REPLACE([SĐT_người_bán],N' Gọi ngay',''),
[Tên_xe]= REPLACE([Tên_xe],LEFT([Tên_xe],7),'') + ' ' + SUBSTRING([Tên_xe],1,4)

UPDATE Oto
SET [Đơn_giá] = CONVERT(BIGINT, REPLACE(REPLACE([Đơn_giá],' ', ''), N'triệu', '000000'))
where [Đơn_giá] not like N'%tỉ%' and 
	  [Đơn_giá] not like '%.%' 

UPDATE Oto
SET [Đơn_giá] = (CAST(LEFT([Đơn_giá], CHARINDEX(N' tỉ', [Đơn_giá]) - 1) AS BIGINT) * 1000000000) +
		(CAST(SUBSTRING([Đơn_giá], CHARINDEX(N' triệu', [Đơn_giá]) - 3, 3) AS BIGINT) * 1000000)
where [Đơn_giá] like N'%tỉ%'

UPDATE Oto
SET [Đơn_giá] = CONVERT(int, REPLACE(REPLACE(REPLACE([Đơn_giá],' ', ''), N'triệu', '00000'),'.',''))
where [Đơn_giá] not like N'%tỉ%' and [Đơn_giá] like '%.%' 

--Thêm cột Hãng xe--
ALTER TABLE Oto
ADD [Hãng_xe] nvarchar(30)

UPDATE Oto
SET [Hãng_xe]= RTRIM(LTRIM(SUBSTRING([Tên_xe],1,CHARINDEX(' ', [Tên_xe]))))

Select * from Oto
