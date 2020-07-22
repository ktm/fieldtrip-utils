import tarfile
import os.path
import shutil
import fieldtripdb
import jpeg


def clean():
    shutil.rmtree('test/tmp/', 1)
    os.mkdir('test/tmp')


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def copy_db_file():
    shutil.copyfile('db/fieldtrip-test.db', 'test/tmp/fieldtrip-test.db')


def create_image_file(field_trip_id, name, lat, lng):
    file_name = 'test/tmp/' + name
    jpeg.createImage(file_name, name, lat, lng, 1000)
    fieldtripdb.create_artifact('test/tmp/fieldtrip-test.db', field_trip_id, lat, lng, file_name+'.jpg', 'test artifacts')


def create_image(field_trip_id, location_id):
    result = fieldtripdb.get_location('test/tmp/fieldtrip-test.db', location_id)
    idkey = result[0].keys().index('id')
    namekey = result[0].keys().index('name')
    latkey = result[0].keys().index('latitude')
    longkey = result[0].keys().index('longitude')
    for row in result:
        create_image_file(field_trip_id, row[namekey], row[latkey], row[longkey])



def create_test_images():
    result = fieldtripdb.get_fieldtrips('test/tmp/fieldtrip-test.db')
    idkey = result[0].keys().index('id')
    locationkey = result[0].keys().index('locationId')

    for row in result:
        create_image(row[idkey], row[locationkey])


clean()
copy_db_file()
create_test_images()
make_tarfile('test/tarball/tarball.tar.gz', 'test/tmp')

# open DB
#   copy DB
#   create some test images
#   add test image meta data to DB copy
#   tarball the lot and move to test/tarball
