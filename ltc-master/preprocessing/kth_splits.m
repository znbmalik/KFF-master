
%cd '../datasets/UCF101/splits';
cd '../datasets/KTH-Datasets/Full-FlowRGB-Peak-KTH-01/splits';
for sp = 1:1
    
    system(['while read p; do mkdir -p split' num2str(sp) '/train/$p; done < ../annot/class_names.txt']);
    system(['while read p; do mkdir -p split' num2str(sp) '/test/$p; done < ../annot/class_names.txt']);
    
    p_train = textread(['../annot/kthTrainTestlist/trainlist0' num2str(sp) '.txt'], '%s');
    for i=1:length(p_train)
        disp([num2str(i) '/' num2str(length(p_train)) ' done.']);
        system(['touch split' num2str(sp) '/train/' p_train{i}]);
    end
    
    p_test = textread(['../annot/kthTrainTestlist/testlist0' num2str(sp) '.txt'], '%s');
    for i=1:length(p_test)
        system(['touch split' num2str(sp) '/test/' p_test{i}]);
    end
    
end

