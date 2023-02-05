---
layout: center
class: "text-center"
---

## Activation Functions

> How to fire the nodes ("neurones") in the next layer, depending on the biases, activation and weights of
the nodes in the previous layer

<style>
h2 {
  margin-bottom: 1.5rem;
}
</style>

---
layout: center
class: "text-justify"
---

The excitation $e$ of the next node is calculated like this: $e = \sum w_i \times a_i + b$

The activation function is a function taking $e$ (the excitation of the node) and mapping it onto
an activation of the node in the next layer.

---
layout: two-cols
---

<div class="h-100 flex flex-col items-center gap-2">

## ReLU
<a href="https://www.desmos.com/calculator/cccdapz4e9" target="_blank" class="h-1/2">
<img src="/images/Relu_Activation.svg" class="h-full"/>
</a>

## SeLU
<a href="https://www.desmos.com/calculator/cccdapz4e9" target="_blank" class="h-1/2">
  <img src="/images/Selu_Activation.svg" class="h-full" />
</a>


</div>
::right::

<div class="h-100 flex flex-col items-center gap-2">

## Tanh
<a href="https://www.desmos.com/calculator/cccdapz4e9" target="_blank" class="h-1/2">
<img src="/images/Tanh_Activation.svg" class="h-full" />
</a>

## Sigmoid
<a href="https://www.desmos.com/calculator/cccdapz4e9" target="_blank" class="h-1/2">
<img src="/images/Sigmoid_Activation.svg" class="h-full" />
</a>

</div>

