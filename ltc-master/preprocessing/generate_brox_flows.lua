require 'torch'
require 'paths'

baseDir = '../datasets/UCF101/UCF-101/'
outputDir = '../datasets/UCF101/flow/jpg/'

for class in paths.iterdirs(baseDir) do
    
    print(class)
    classPath=paths.concat(baseDir,class)
    
    for videoName in paths.files(classPath) do
	
        videoPath=paths.concat(classPath,videoName)
        print(videoPath)


        flowPath=paths.concat(outputDir,class,videoName)
        local str = flowPath
	local flowPath = str:match("(.+)%..+")
	print(flowPath)


	os.execute('../flow_toolbox-master/flow_video -b 5 -e 10 -o '+videoPath+' '+flowPath)
	break
    end
end

