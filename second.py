#! C:/Users/IBM_ADMIN/PycharmProjects/WebScraping_Html/venv/Scripts/python.exe
# Import modules for CGI handling
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 


print("Content-type:text/html\r\n\r\n")




print("<form action = 'Neo4jQA_enhance.py' method = 'post'>")
print("<h2>Type your Query below</h2><br />")
print("<h3>['acer e110', 'acer liquid a1', 'acer liquid e', 'alcatel one touch 980', 'asus padfone', 'blackberry keyone', 'blackberry motion', 'nexus one', 'galaxy nexus', 'nexus 4', 'nexus 5x', 'nexus 6p', 'htc aria', 'htc desire eye', 'htc dream', 'htc inspire 4g', 'htc evo 4g lte', 'htc hero', 'htc incredible s', 'htc one', 'alcatel one touch 990', 'blackberry priv', 'blackberry dtek50', 'blackberry dtek60', 'nexus s', 'htc ruby', 'lg g flex 2', 'lg g4', 'oneplus 5t', 'samsung galaxy beam i8530', 'samsung galaxy core', 'samsung galaxy core lte', 'samsung galaxy mini 2', 'samsung galaxy pocket', 'samsung galaxy pocket plus', 'samsung i9070 galaxy s advance', 'samsung galaxy s duos', 'samsung galaxy s5 mini', 'sony xperia e', 'sony xperia go', 'htc desire', 'htc desire 620', 'htc desire hd', 'htc desire s', 'htc desire z', 'htc evo 4g', 'htc butterfly', 'huawei mate 9', 'lg g2 mini', 'lg g3 stylus', 'lg gx', 'lg optimus gt540', 'lg optimus 4x hd p880', 'lg optimus chic e720', 'lg optimus q lu2300', 'lg optimus vu ii', 'meizu pro 5', 'meizu mx', 'meizu mx4', 'meizu mx4 pro', 'htc desire x', 'htc droid incredible', 'droid incredible 4g lte', 'htc evo shift 4g', 'htc evo design 4g', 'htc evo 3d', 'htc explorer', 'htc legend', 'htc one s', 'htc one v', 'htc one mini 2', 'htc one max', 'htc 10', 'huawei ideos u8150', 'huawei u8800 ideos x5', 'huawei sonic', 'huawei p10', 'huawei mate s', 'huawei mate 8', 'lg g2', 'htc one m9', 'htc one mini', 'htc rezound', 'htc tattoo', 'htc thunderbolt', 'htc u ultra', 'huawei nova', 'razer phone', 'sony ericsson xperia ray', 'sony ericsson xperia x8', 'sony ericsson xperia x10', 'xiaomi mi2', 'xiaomi mi 2a', 'xiaomi mi 2s', 'xiaomi mi 3', 'xiaomi mi 4', 'xiaomi redmi note 2', 'xiaomi redmi note 4', 'zte', 'zte engage', 'lg g3', 'lg g flex', 'lg g pro 2', 'lg g pro lite', 'lg optimus black', 'lg optimus g', 'lg optimus l9 p760', 'lg optimus one', 'lg optimus vu', 'lg v10', 'lg v20', 'meizu m9', 'meizu mx3', 'amazon fire phone', 'ubuntu edge', 'dell venue', 'garmin nüvifone', 'geeksphone one', 'kyocera echo', 'nextbit robin', 'meizu mx5', 'essential phone', 'vertu ti', 'motorola atrix 4g', 'motorola atrix 2', 'droid 4', 'droid razr', 'moto g', 'moto e', 'moto z', 'moto z play', 'nokia 7', 'nokia 8', 'nokia x', 'nokia xl', 'nokia x2', 'oneplus x', 'sony ericsson xperia pro', 'sony ericsson xperia x10 mini', 'xiaomi mi4i', 'pepsi p1 and p1s', 'motorola backflip', 'motorola charm', 'motorola defy a8210', 'droid bionic', 'motorola flipout', 'motorola i1', 'moto x', 'moto x style', 'moto x play', 'moto x4 1', 'moto g5', 'moto e 2nd generation', 'nokia 3', 'nokia 5', 'oneplus one', 'oneplus 2', 'oneplus 3', 'oneplus 3t', 'oneplus 5', 'samsung galaxy s glide', 'samsung galaxy 3', 'galaxy ace 4', 'samsung galaxy alpha', 'samsung galaxy a5', 'samsung galaxy a9', 'samsung galaxy fit', 'samsung galaxy round', 'samsung galaxy s', 'samsung galaxy s plus', 'samsung galaxy s 4g lte', 'samsung galaxy s ii', 'samsung galaxy s iii mini', 'samsung galaxy s4', 'samsung galaxy s4 mini', 'samsung galaxy s4 active', 'samsung galaxy s5', 'samsung galaxy s6 active', 'samsung galaxy w', 'samsung galaxy win', 'sony xperia c3', 'sony xperia c4', 'sony xperia ion', 'sony xperia p', 'sony xperia sola', 'sony xperia sp', 'sony xperia t', 'sony xperia u', 'sony xperia x', 'sony xperia xa ultra', 'sony xperia xa1', 'sony xperia x performance', 'sony xperia x compact', 'sony xperia xz', 'sony xperia xz premium', 'sony xperia z', 'sony xperia zl', 'sony xperia e1', 'sony xperia z3', 'sony xperia z3 compact', 'sony xperia m', 'sony xperia', 'sony xperia v', 'sony xperia xa', 'sony xperia xzs', 'sony xperia zr', 'sony xperia z1', 'sony xperia z1 compact', 'sony xperia z2', 'sony xperia e3', 'sony xperia e4', 'sony xperia z5 premium', 'sony xperia e5', 'sony ericsson xperia acro', 'sony ericsson xperia mini', 'sony ericsson xperia neo', 'sony ericsson xperia neo v', 'sony ericsson xperia play', 'sony xperia z5', 'sony xperia z5 compact', 'sony ericsson xperia arc s lt18i', 'sony ericsson xperia mini pro', 'xiaomi mi 4c', 'xiaomi mi mix', 'xiaomi mi mix 2', 'xiaomi redmi 1s', 'xiaomi redmi note 3', 'zte racer', 'zte skate']</h3><br/>")
print("Enter Query: <input type = 'text' name = 'Query' />")

print('<input type = "submit" value = "Submit" />')
print("</form>")