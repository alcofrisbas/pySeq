fun void writeInts(int integers[], string path) {
	FileIO file;
	if (!file.open(path, FileIO.MODE_WRITEONLY | FileIO.MODE_BINARY))
		return;

	file <~ integers.size();
	for (0=>int i; i< integers.size(); i++)
		file <~ integers[i];

	file.close();
}

writeInts([1,0,0,0], "intTest.txt");
