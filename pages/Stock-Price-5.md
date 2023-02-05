---
layout: center
class: "text-center"
---

## LSTMs

> An advanced RNN with memory cells that resolve inherent problems of RNNs.

<style>
h2 {
  margin-bottom: 1.5rem;
}
</style>

---
layout: center
class: "text-justify"
---

<div class="flex flex-col items-center">

<div>

The classic RNN has an issue that is both known as the
**Vanishing Gradient Problem** or **Exploding Gradient Problem**.
The first happens when the activation $a$ is between $0$ and $1$, the
second when $a$ is bigger than $1$. Due to the feedback, the influence
of of older inputs is either disappearing - killing the effect of learning
from long learn trends in the input data - or exploding and overshadowing
newer inputs.

One of the solutions to this issue is the LSTM (Long Short-Term Memory) network.
It has adjustments inside the core RNN layer that allow it to forget irrelevant information
and more strongly remember information from older inputs, solving the main issue
from a classical RNN. This comes at a cost of longer computation, resulting
in longer or more computationally intensive training of the model.

</div>

![](/images/LSTMs.png)

</div>

<style>
img {
  max-width: 600px;
}
</style>
