require 'nn'
local model = {}
table.insert(model, {'data', nn.VolumetricMaxPooling(0, 0, 0, 1, 1, 1, 0, 0, 0):ceil()})
table.insert(model, {'conv1a', nn.VolumetricConvolution(3, 64, 3, 3, 3, 1, 1, 1, 1, 1, 1)})
table.insert(model, {'relu1a', nn.ReLU(true)})
table.insert(model, {'pool1', nn.VolumetricMaxPooling(1, 2, 2, 1, 2, 2, 0, 0, 0):ceil()})
table.insert(model, {'conv2a', nn.VolumetricConvolution(64, 128, 3, 3, 3, 1, 1, 1, 1, 1, 1)})
table.insert(model, {'relu2a', nn.ReLU(true)})
table.insert(model, {'pool2', nn.VolumetricMaxPooling(2, 2, 2, 2, 2, 2, 0, 0, 0):ceil()})
table.insert(model, {'conv3a', nn.VolumetricConvolution(128, 256, 3, 3, 3, 1, 1, 1, 1, 1, 1)})
table.insert(model, {'relu3a', nn.ReLU(true)})
table.insert(model, {'conv3b', nn.VolumetricConvolution(256, 256, 3, 3, 3, 1, 1, 1, 1, 1, 1)})
table.insert(model, {'relu3b', nn.ReLU(true)})
table.insert(model, {'pool3', nn.VolumetricMaxPooling(2, 2, 2, 2, 2, 2, 0, 0, 0):ceil()})
table.insert(model, {'conv4a', nn.VolumetricConvolution(256, 512, 3, 3, 3, 1, 1, 1, 1, 1, 1)})
table.insert(model, {'relu4a', nn.ReLU(true)})
table.insert(model, {'conv4b', nn.VolumetricConvolution(512, 512, 3, 3, 3, 1, 1, 1, 1, 1, 1)})
table.insert(model, {'relu4b', nn.ReLU(true)})
table.insert(model, {'pool4', nn.VolumetricMaxPooling(2, 2, 2, 2, 2, 2, 0, 0, 0):ceil()})
table.insert(model, {'conv5a', nn.VolumetricConvolution(512, 512, 3, 3, 3, 1, 1, 1, 1, 1, 1)})
table.insert(model, {'relu5a', nn.ReLU(true)})
table.insert(model, {'conv5b', nn.VolumetricConvolution(512, 512, 3, 3, 3, 1, 1, 1, 1, 1, 1)})
table.insert(model, {'relu5b', nn.ReLU(true)})
table.insert(model, {'pool5', nn.VolumetricMaxPooling(2, 2, 2, 2, 2, 2, 0, 0, 0):ceil()})
table.insert(model, {'torch_view', nn.View(-1):setNumInputDims(3)})
table.insert(model, {'fc6-1', nn.Linear(8192, 4096)})
table.insert(model, {'relu6', nn.ReLU(true)})
table.insert(model, {'drop6', nn.Dropout(0.500000)})
table.insert(model, {'fc7-1', nn.Linear(4096, 4096)})
table.insert(model, {'relu7', nn.ReLU(true)})
table.insert(model, {'drop7', nn.Dropout(0.500000)})
table.insert(model, {'fc8-1', nn.Linear(4096, 487)})
table.insert(model, {'loss', nn.SoftMax()})
return model