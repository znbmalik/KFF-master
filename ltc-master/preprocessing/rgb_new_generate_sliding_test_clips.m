clear; clc;

dataRoot = '../datasets/Full-Flow-KFF-JHMDB/';
disp("hello")
disp(dir(dataRoot))
% Loop over three splits
for split = 1:1
    testDir = fullfile(dataRoot, 'splits', sprintf('split%d', split), 'test');
    disp(testDir)
    % Loop over possible window sizes
    for W = 16
        % Loop over possible skips
        for skip = 4
            targetDir = fullfile(dataRoot, 'splits', sprintf('split%d', split), sprintf('test_%d_%d', W, skip));
            disp(targetDir)
            classes = dir(testDir);
            disp(classes)
            classes = classes([classes.isdir]);
            disp(classes)
            classes = classes(arrayfun(@(x) x.name(1), classes) ~= '.');
            
            C = length(classes);
            
            disp(C)
            for class = 1:C
                disp(['Class: ' num2str(class) ' ' classes(class).name]);
                system(sprintf('mkdir -p ''%s''', fullfile(targetDir, classes(class).name)));
                videos = dir(fullfile(testDir, classes(class).name, '*.avi'));
                V = length(videos);
                for video = 1:V
                    disp(['Class' num2str(class) ': ' classes(class).name ' - Video' num2str(video) ': ' videos(video).name]);
                    frames = dir(fullfile(dataRoot, 'rgb', 'jpg', classes(class).name, videos(video).name, '*.jpg'));
                    totalDuration = length(frames); % note: nFlow = nRGB -1
                    disp(fullfile(dataRoot, 'rgb', 'jpg', classes(class).name, videos(video).name, '*.jpg'))
                    disp(totalDuration)
                    nClips = ceil((totalDuration - W)/skip) + 1;
                    if(totalDuration < W)
                        nClips = 1;
                            system(sprintf('touch ''%s_%04d.avi''',  fullfile(targetDir, classes(class).name, videos(video).name), 1));
                    end
                    for tt = 1:nClips
                            system(sprintf('touch ''%s_%04d.avi''',  fullfile(targetDir, classes(class).name, videos(video).name), tt));
                    end
                end
            end
        end
    end
end