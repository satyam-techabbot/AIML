# **Transfer Learning**

> It is a technique where a model trained on one task is reused for similar related task especially when new task has limited data.

--- 

### Advantages: 
- Uses learned features from first task
- Reduces training time for new task
- Improves accuracy with lesser data
- Uses general features

---

## Importance

- **Limited Data:**
    > Enables us to use pretrained models which decreases dependencies on large datasets
- **Enhance Performance:**
    > using pre-trained model which already have important features improves the accuracy and efficiency
- **Time and Cost Efficiency:**
    > It shortens time and conserves resources by using pre-trained model and need of big dataset saves money.
- **Adaptability:**
    > New task model adapts features of first task

---

## Working of Transfer learning

1. **Pre-Trained Model:**
    > General Features and patterns that are relevant to specific task.
2. **Base Model:**
    > This pre-trained model, known as the base model, includes layers that have processed data to learn hierarchical representations, capturing low-level to complex features.
3. **Transfer Layers:**
    > Identify layers within the base model that hold generic information applicable to both the original and new tasks. Lower layers capture general features such as edges and textures, while higher layers capture task-specific complex patterns.
4. **Fine-tuning:**
    > Fine-tune these selected layers with data from the new task. This process helps retain the pre-trained knowledge while adjusting parameters to meet the specific requirements of the new task, improving accuracy and adaptability.

### **Frozen and Trainable** 
| **Aspect** | **Frozen Layers** | **Trainable Layers** | 
| ------ | -------- | --- |
| Definition | Layers whose weights are kept fixed and not updated during training | Layers whose weights are updated during training |
| Purpose | Preserve general features learned from large pre-trained datasets | Adapt to task-specific features of the new dataset
| Learning Process | No backpropagation updates; remain constant | Updated through backpropagation based on new data
| Use Case | Used when new dataset is small or similar to the original dataset | Used when new dataset is large or significantly different from the original task
| Computation Cost | Lower, since fewer parameters are trained | Higher, as more parameters need to be updated
|  Example in CNN |  Early convolutional layers that capture edges, textures and basic shapes |  Later fully connected layers or deeper convolutional layers for fine-tuned features


### **How to Decide Which Layers to Freeze or Train**
The extent to which you freeze or fine-tune layers depends on the similarity and size of your target dataset:

- Small, Similar Dataset: For smaller datasets that resemble the original dataset, you freeze most layers and only fine-tune the last one or two layers to prevent overfitting.

- Large, Similar Dataset: With large, similar datasets you can unfreeze more layers allowing the model to adapt while retaining learned features from the base model.

- Small, Different Dataset: For smaller, dissimilar datasets, fine-tuning layers closer to the input layer helps the model learn task-specific features from scratch.

- Large, Different Dataset: In this case, fine-tuning the entire model helps the model adapt to the new task while using the broad knowledge from the pre-trained model.


---

## **Transfer Learning with MobileNetV2 for MNIST Classification**










