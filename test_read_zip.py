import zipfile

exceptions = []
with zipfile.ZipFile("data/dnd_srd_wiki.zip", "r") as zip_file:
    infos = zip_file.infolist()
    for info in infos:
        try:
            byte_data = zip_file.read(info.filename)
            text = byte_data.decode("utf-8")
            print("\n--------------------")
            print(text.strip().replace("\n", " "))
        except Exception as ex:
            exceptions.append(ex)

print(f"\n{len(exceptions)=}")
