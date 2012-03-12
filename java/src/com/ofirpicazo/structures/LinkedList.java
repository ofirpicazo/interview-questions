// 
package com.ofirpicazo.structures;

/**
 * Implementation of a simple single linked list.
 * @author ofirp
 *
 */
public class LinkedList<T> {
    private ListNode<T> firstNode;
    private ListNode<T> currentNode;

    public LinkedList() {
        firstNode = new ListNode<T>();
    }

    /**
     * Add a new node at the end of the list.
     * @param newNode
     */
    public void add(ListNode<T> newNode) {
        currentNode = firstNode;
        while (currentNode.hasNext()) {
            currentNode = currentNode.getNext();
        }
        currentNode.setNext(newNode);
    }
    
    public void delete(T value) {
        ListNode<T> runnerNode = null;
        currentNode = firstNode;

        while (currentNode.hasNext()) {
            if (currentNode.getValue() == value) {
                if (runnerNode != null) {
                    runnerNode.setNext(currentNode.getNext());
                } else {
                    firstNode = currentNode.getNext();
                }
            } else {
                runnerNode = currentNode;
                currentNode = currentNode.getNext();
            }
        }
    }
    
    public String toString() {
        StringBuffer sb = new StringBuffer();
        currentNode = firstNode;
        while (currentNode.hasNext()) {
            sb.append(currentNode.getValue());
        }
        return sb.toString();
    }
}

class ListNode<T> {
    private T value;
    private ListNode<T> nextNode;

    public ListNode() {}
    
    public ListNode(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }
    
    public ListNode<T> getNext() {
        return nextNode;
    }
    
    public void setNext(ListNode<T> node) {
        this.nextNode = node;
    }
    
    public boolean hasNext() {
        return (this.nextNode == null) ? true : false;
    }
    
    public String toString() {
        return value.toString();
    }
}