---
layout: center
class: "text-center"
---

## RNNs

> A neural network model with a feedback loop.

<style>
h2 {
  margin-bottom: 1.5rem;
}
</style>

---
layout: center
class: "text-justify"
---

<div class="flex items-center gap-8">

While classical feedforward network models have data flow only in one direction (that is from input
layer to output layer and from output to input layer during backpropagation),
RNNs - or Recurrent Neural Networks - implement a mechanism for the last input to effect the
next one. They do this by introducing the concept of time. Instead of having a single propagation
through the network, inputs are fed into the network one after the other. The following time steps
enable us to let inputs influence each other by feeding the output of the hidden RNN layer back into
itself as an input during the next iteration.

![](/images/RNNs.png)

</div>

<style>
img {
  min-width: 350px;
}
</style>

---
layout: center
class: "text-justify"
---

They are especially handy when the number of input is not known at compile time. For example, when we 
analyse images, we might know that all our images are in the format 128x128 pixel, resulting in a flattened
input layer with $128 \times 128 = 16384$ input nodes.

When we analyse stock data, how many input nodes are required? We won't know beforehand, if the stock will
have 200 days of data or 50. A classical feedforward network can't handle a dynamic number of inputs,
a RNN can.

The feedback can also pick up on long-term trends that are hidden inside the data of the stock price. This
can be generally said about time-series data, which RNNs excel at, if it is stock market data, temperature
or humidity measurements or a countries yearly spending on education programs.

