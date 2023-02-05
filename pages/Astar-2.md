---
layout: two-cols
---

## Pseudo-Code

```typescript
// Priority queue of open nodes
declare openlist as PriorityQueue with Nodes
declare closedlist as Set with Nodes

program a-star
    // Add start node to the open list
    openlist.enqueue(startNode, 0)
    repeat  
        // get next node from open list with
        // lowest f-value
        currentNode := openlist.removeMin()

        if currentNode == zielknoten then
            return PathFound
        // add current node to closed list to
        // not visit it again
        closedlist.add(currentNode)

        // call subroutine "expandNode"
        expandNode(currentNode)
    until openlist.isEmpty()
    // path could not be determined
    return NoPathFound
end
```

::right::

## Implementation (Rust)

```rust
pub fn generate_a_star_solution( /* ... */)
-> Option<Vec<Node>> {
    // initialize open list with start node
    let mut open_list: BinaryHeap<Node> =
    binary_heap::BinaryHeap::new();
    open_list.push(start_node);
    let mut closed_list: Vec<Node> = vec![];

    // iterate over open nodes
    while let Some(current_node) = open_list.pop() {
        // Don't visit node twice
        closed_list.push(current_node.clone());

        // shortest path was found
        if current_node.name == target_node.name {
            return Some(closed_list);
        }

        // add neighbour nodes to open list
        expand_node( /* ... */ );
    }
    // path could not be determined
    None
}
```


<style>
code {
  @apply text-teal-500 dark:text-teal-400;
}
</style>
