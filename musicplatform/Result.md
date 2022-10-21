# Task1
### 1- create some artists
	code:
     >>> python manage.py shell
     >>> from artists.models import Artist
     >>> object = Artist(stagename = 'stage1', sociallink='www.stage1.com')
     >>> object.save()
	 >>> object = Artist(stagename = 'Mohamed Khedr', sociallink='www.mKhedr.com')
	 >>> object.save()
     >>> object = Artist(stagename = 'Ahmed Mohamed', sociallink='www.aMohamed.com')
     >>> object.save()
     >>> object = Artist(stagename = 'Hesham Mohamed', sociallink='www.hMohamed.com')
     >>> object.save()
  
### 2- list down all artists
	code:
	 >>> Artist.objects.all()
	
	result:
	 <QuerySet  [<Artist:  Stage1>, <Artist:  stage1>, <Artist:  Mohamed  Khedr>, <Artist:  Ahmed  Mohamed>, <Artist:  Hesham  Mohamed>]>



### 3-  list down all artists sorted by name
	code: 
	 >>> Artist.objects.order_by('stagename')
	
	result:
	 <QuerySet  [<Artist:  Ahmed  Mohamed>, <Artist:  Hesham  Mohamed>, <Artist:  Mohamed  Khedr>, <Artist:  Stage1>, <Artist:  stage1>]>

 

### 4- list down all artists whose name starts with  `a`
	code:
	 >>> Artist.objects.filter(stagename__startswith='a')
	 
	result:
	 <QuerySet  [<Artist:  Ahmed  Mohamed>]>

### 5-   in 2 different ways, create some albums and assign them to any artists (hint: use  `objects`  manager and use the related object reference)
	Way#1 code:
	 >>> TamerHosny = Artist(stagename = 'Tamer Hosny', sociallink = 'www.tHosny.com') 
	 >>> TamerHosny.save()
	 >>> arrabkaman  = Album(AlbumArtist = TamerHosny, AlbumName = 'ArrabKaman', CreationDate = datetime.date(2018,6,20), ReleaseDate = 
	datetime.date(2019,1,1), Price = 30)
	 >>> arrabkaman.save()
	 >>> elygaiahla  = Album(AlbumArtist = TamerHosny, AlbumName = 'elygaiahla', CreationDate = 	datetime.date(2011,4,30), ReleaseDate = 
	datetime.date(2012,12,2), Price = 50)
	 >>> elygaiahla.save()

	Way#2 code:
	 >>> AmrDiab  = Artist(stagename = 'AmrDiab', sociallink = 'www.aDiab.com')
	 >>> AmrDiab.save()
	 >>> Album.objects.create(AlbumArtist = AmrDiab, AlbumName = 'tamalymaak', CreationDate = datetime.date(2000,5,20), ReleaseDate = datetime.date(2000,6,30), Price = 75)
	 >>> Album.objects.create(AlbumArtist = AmrDiab, AlbumName = 'Wayyah', CreationDate = datetime.date(2010,7,2), ReleaseDate = datetime.date(2011,11,20), Price = 70)
	

### 6-   get the latest released album
	code:
	 >>> Album.objects.latest('ReleaseDate') 
	 
	result:
	 <Album: ArrabKaman>

### 7-   get all albums released before today
	code:
	 >>> Album.objects.filter( ReleaseDate__lt=date.today()) 
	 
	result:
	 <QuerySet [<Album: ArrabKaman>,  <Album: elygaiahla>, <Album: Wayyah>, <Album: tamalymaak>]>

### 8-   get all albums released today or before but not after today
	code:
	 >>> Album.objects.filter( ReleaseDate__lte=date.today()) 
	 
	result:
	 <QuerySet [<Album: ArrabKaman>,  <Album: elygaiahla>, <Album: Wayyah>, <Album: tamalymaak>]>
### 9-   count the total number of albums (hint: count in an optimized manner)
	code:
	 >>> Album.objects.count()
	 
	result:
	 4
### 10-   in 2 different ways, for each artist, list down all of his/her albums (hint: use  `objects`  manager and use the related object reference)
	Way#1 code:
	 >>> [artist.album_set.all() for artist in Artist.objects.all()]
	 
	Way#1 result: 
	 <QuerySet [<Album: ArrabKaman>,  <Album: elygaiahla>, <Album: Wayyah>, <Album: tamalymaak>]>
	
	Way#2 code:
	 >>> [Album.objects.filter(AlbumArtist_id=artist.id) for artist in Artist.objects.all()]
	 
	Way#2 result:
	 <QuerySet [<Album: ArrabKaman>,  <Album: elygaiahla>, <Album: Wayyah>, <Album: tamalymaak>]> 

### 11-   list down all albums ordered by cost then by name (cost has the higher priority)
	code:
	 >>> Album.objects.order_by('Price', 'AlbumName')
   
	result:
	 <QuerySet [<Album: ArrabKaman>,  <Album: elygaiahla>, <Album: Wayyah>, <Album: tamalymaak>]> 
