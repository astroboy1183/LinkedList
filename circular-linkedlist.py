class CircularLinkedList:
	def __init__(self):
		
		self.head=None


	def PrintNodes(self):
		
		p=self.head

		if(p is None):

			print("No Nodes are present!!")

		else:
			out=''
			print(p.data)
			p=p.next
			print(p.data)
			p=p.next
			print(p.data)
			flag=0
			while(p is not self.head or flag==0):
				out+=str(p.data)+'<->'
				print('printing')
				p=p.next
				flag=1

			return out

	def push(self,value):

		p=self.head
		q=self.head
		if(p is None):
			print('No nodes present , creating first node!!')
			self.append(value)
			return
	   
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node
		while(q is not self.head):
			q=q.next
		q.next=new_node

	def append(self,value):
		p=self.head
		if(p is None):
			new_node = Node(value)
			self.head = new_node
			new_node.next=self.head
			return
		new_node = Node(value)
		print('appending')
		while(p is not self.head):
			p=p.next
		p.next=new_node
		new_node.next=self.head
		self.head.next=self.head
		print('appended')



	def insertafter(self,prev_value,value):
		p=self.head
		while(p.next is not None):
			if(p.data==prev_value):
				new_node = Node(value)
				new_node.next=p.next
				p.next.prev=new_node
				new_node.prev=p
				p.next=new_node
				return

			else:
				p=p.next
		if(p is not None and p.next is None):
			print('cannot insert node as previous value is not present!! Inserting node at END OF THE LIST!!')
			llist.append(value)
			return
		# if(p.next is None):
			
		# 	llist.append(value)
		# 	return

	def deletenode(self,value):
		p=self.head
		if(p is None):
			print('linked list is empty!!')
			return
		else:
			if(p.data==value):
				if(p.next is not None):
					self.head=p.next
					p.next.prev=None
				else:
					self.head=None
					print('linked list is now empty!!')
				return
			else:
				while(p is not None):
					if(p.data==value):
						break
					p=p.next
					# print('moving pointer')

				if(p is None):
					print('Element not found in linked list!!')
					return
				if(p.next is None):
					p.prev.next=None
					p.prev=None
					p=None
					return
				p.next.prev=p.prev
				# print('deleting ',p.data)
				p.prev.next=p.next
				p=None
			# print(self.PrintNodes())

	def sumnodes(self):
		p=self.head
		sum=0
		while(p):
			sum+=p.data
			p=p.next
		return sum

	def count(self):
		p=self.head
		if(p is None):
			return 0;
		else:
			count=0
			while(p):
				count+=1
				p=p.next

			return count

	def findmax(self):
		p=self.head
		if(p is None):
			return "no elements" 
		else:
			max1=p.data
			while(p is not None):
				if(p.data>max1):
					max1=p.data
				p=p.next
			return max1

	def search(self,value):
		p=self.head
		count=1
		print("Elements found at positions:\n")
		while(p is not None):
			if(p.data==value):
				print(count)
			p=p.next
			count+=1 
	
	
	def sort(self,key):
		p=self.head
		q=self.head
		if(p is None):
			print("No nodes in the linked list!!")
			return
		if(llist.count()==1):
			print(self.PrintNodes())
			return
		while(p is not None):
			q=p.next
			while(q is not None):
				if (key=='asc'):
					if(p.data>q.data):
						p.data,q.data=q.data,p.data
				else:
					if(p.data<=q.data):
						p.data,q.data=q.data,p.data
				q=q.next
			p=p.next
		print(self.PrintNodes())


	def checksorted(self):
		p=self.head
		q=self.head
		asc=0
		desc=0
		if(p is None):
			print("No element is present!!")
			return
		else:
			while(p is not None):
				q=p.next
				if(q is not None):
					if(p.data>q.data):
						desc+=1
					else:
						asc+=1
				p=p.next
		print(asc,desc)
		if(asc==0 or desc==0):
			print('sorted')
			return
		else:
			print('not sorted')
			return

	def removeduplicates_unsorted(self):
		p=self.head
		if(p is None):
			print("No nodes in the list!!")
			return
		else:
			max_ele = self.findmax()
			hashmap=[0]*(max_ele+1)
			while(p is not None):
				hashmap[p.data]+=1
				p=p.next
			delete_ele=[]
			count=[]
			#{224:2,22:4}
			for i in range(len(hashmap)):
				if(hashmap[i]>1):
					delete_ele.append(i)
					count.append(hashmap[i])
			print(delete_ele)
			if(len(delete_ele)==0):
				print('No duplicates!!')
				return
			else:
				for i in range(len(delete_ele)):
					for j in range(count[i]):
						self.deletenode(delete_ele[i])
			print('duplicates deleted!!')
			return

	def removeduplicates_sorted(self):
		p=self.head
		q=self.head
		if(p is None):
			print("No nodes in the list!!")
			return
		else:
			self.sort('asc')
			c=0
			while(p is not None and p.next is not None):
				if(c==0):
					q=p.next
				if(p.data==q.data):
					self.deletenode(q.data)
					q=p.next.next
					p=p.next
					self.deletenode(p.data)
					c=1
				else:
					c=0

				p=p.next
			print('duplicates deleted!!')
			return

	def reverselist(self):
		p=self.head
		q=self.head

		if(p is None):
			print("no nodes in the list!!")
			return
		else:
			while(q.next):
				q=q.next
			# pcount=0
			# qcount=self.count()-1
			exchanges = math.ceil(self.count()/2)
			c=0
			while(p!=q and c<=exchanges):
				if(p.next is not None and q.prev is not None):
					p.data,q.data = q.data,p.data
					# pcount+=1
					# qcount-=1
					p=p.next
					q=q.prev
					c+=1
				else:
					return	

class Node:
	def __init__(self,data):
		
		self.data = data
		
		self.next = None



if __name__=='__main__':

	llist=CircularLinkedList()
while(1):
	inp=input('Please enter your choice:\n 1.insert 2.delete 3.count, 4.sum, 5.print nodes, 6.find maximum element, 7.Search element, 8.sort the linked list in ascending order,9.sort the linked list in descending order , 10. check if linked list is sorted, 11. remove duplicates unsorted ,12. remove duplicates sorted ,13. Print Nodes Reverse ,14.exit\n')
	if(inp=='1'):
		inp1 = input('1.insert at start, 2. insert after a particular node, 3.insert at end')
		if(inp1=='1'):
			inp2=input('Enter the value to insert:')
			llist.push(int(inp2))
		elif(inp1=='2'):
			if(llist.count()==0):
				print("No nodes are present. Please add a node!!")
				inp2=input("Enter a value to insert!!")
				llist.append(int(inp2))
			else:
				inp3=input('Enter value to insert')
				inp4=input('Enter previous value of node')
				llist.insertafter(int(inp4),int(inp3))

		elif(inp1=='3'):
			inp2=input('Enter value to insert')
			llist.append(int(inp2))
		else:
			print('Please Enter a valid option!!')

	elif(inp=='2'):
		if(llist.count()==0):
			print('no nodes to delete!! Please add a node!!')
		else:
			inp1=input('Enter value to delete')
			llist.deletenode(int(inp1))

	elif(inp=='3'):

		count = llist.count()
		print('number of nodes is:',count)

	elif(inp=='4'):
		if(llist.count()==0):
			print('no nodes to perform sum!!')
		else:
			sum = llist.sumnodes()
			print('sum is:',sum)

	elif(inp=='5'):
		out = llist.PrintNodes()
		print(out)

	elif(inp=='6'):
		max1=llist.findmax()
		print("max is:",max1)

	elif(inp=='7'):
		if(llist.count()==0):
			print('Linked List is empty. Cannot perform search!!')
		else:
			inp1=input('Enter the element to search:')
			llist.search(int(inp1))

	elif(inp=='8'):
		llist.sort('asc')

	elif(inp=='9'):
		llist.sort('desc')

	elif(inp=='10'):
		llist.checksorted()

	elif(inp=='11'):
		llist.removeduplicates_unsorted()

	elif(inp=='12'):
		llist.removeduplicates_sorted()

	elif(inp=='13'):
		llist.reverselist()
	
	elif(inp=='14'):
		break

	else:
		print('Please enter a valid option!!')
		# llist.sample()