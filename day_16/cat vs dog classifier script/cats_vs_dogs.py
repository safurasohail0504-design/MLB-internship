import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

print("Cats vs Dogs Classifier (Transfer Learning)")
print("\nInitializing data generator")
num_samples=200
img_height,img_width=160,160
np.random.seed(42)
fake_images=[np.random.randint(0, 256, size=(img_height, img_width, 3), dtype=np.uint8) for _ in range(num_samples)]
fake_labels=np.random.randint(0, 2, size=(num_samples,))
split_idx=int(num_samples * 0.8)
X_train_raw,X_val_raw=fake_images[:split_idx],fake_images[split_idx:]
y_train_raw,y_val_raw=fake_labels[:split_idx],fake_labels[split_idx:]
print("Applying data preprocessing and normalization")
def process_pipeline(img_list,lbl_list):
    processed_imgs=[]
    for img in img_list:
        tensor_img=tf.cast(img,tf.float32)
        normalized_img=(tensor_img/127.5)-1.0
        processed_imgs.append(normalized_img)
    return tf.stack(processed_imgs),tf.convert_to_tensor(lbl_list,dtype=tf.int32)
X_train,y_train=process_pipeline(X_train_raw, y_train_raw)
X_val,y_val=process_pipeline(X_val_raw, y_val_raw)
BATCH_SIZE=32
train_dataset=tf.data.Dataset.from_tensor_slices((X_train,y_train)).shuffle(100).batch(BATCH_SIZE)
val_dataset=tf.data.Dataset.from_tensor_slices((X_val,y_val)).batch(BATCH_SIZE)
print("Loading pre-trained MobileNetV2 backbone")
base_model=tf.keras.applications.MobileNetV2(
    input_shape=(img_height, img_width, 3),
    include_top=False,
    weights="imagenet"
)
base_model.trainable=False
model=models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128,activation='relu'),
    layers.Dropout(0.3),  
    layers.Dense(1,activation='sigmoid') 
])
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)
model.summary()
print("\nStarting training loop")
EPOCHS=5
history=model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=EPOCHS
)
print("\nExtracting evaluations and generating graphs")
acc=history.history['accuracy']
val_acc=history.history['val_accuracy']
loss=history.history['loss']
val_loss=history.history['val_loss']
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(range(1,EPOCHS+1), acc, label='Training Accuracy', marker='o')
plt.plot(range(1,EPOCHS+1), val_acc, label='Validation Accuracy', marker='s')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy Score')
plt.legend()
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(range(1,EPOCHS+1),loss,label='Training Loss',marker='o')
plt.plot(range(1,EPOCHS+1),val_loss,label='Validation Loss',marker='s')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('accuracy_loss_curves.png')
plt.show()
print("\nRendering preview matrix for sample inference evaluation")
class_names=['Cat','Dog']
for images,labels in val_dataset.take(1):
    raw_predictions=model.predict(images)
    predicted_classes=[1 if p > 0.5 else 0 for p in raw_predictions]
    plt.figure(figsize=(10,4))
    for i in range(5):
        plt.subplot(1,5,i+1)
        # Denormalizing pixel maps for direct image plotting
        display_img=((images[i].numpy()+1.0)*127.5).astype(np.uint8)
        plt.imshow(display_img)
        pred_name=class_names[predicted_classes[i]]
        true_name=class_names[labels[i].numpy()]
        plt.title(f"Pred:{pred_name}\nTrue:{true_name}",fontsize=10)
        plt.axis('off')
    plt.tight_layout()
    plt.savefig('sample_predictions.png')
    plt.show()
    break