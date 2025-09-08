const pets = [
    {
      id: 1,
      name: 'Max',
      type: 'Dog',
      breed: 'Labrador',
      age: 2
    },
    {
      id: 2,
      name: 'Bella',
      type: 'Cat',
      breed: 'Siamese',
      age: 3
    },
    {
      id: 3,
      name: 'Charlie',
      type: 'Bird',
      breed: 'Canary',
      age: 1
    }
  ]
  
  const resolvers = {
    Query: {
      pets: () => pets,
      pet: (parent, args) => pets.find(pet => pet.id === args.id)
    },
    Mutation: {
      addPet: (parent, args) => {
        const newPet = {
          id: Date.now(),
          ...args.pet
        }
        pets.push(newPet)
        return newPet
      },
      editPet: (parent, args) => {
        pets = pets.map(pet => (pet.id === args.id ? { ...pet, ...args.pet } : pet))
        return pets.find(pet => pet.id === args.id)
      },
      deletePet: (parent, args) => {
        pets = pets.filter(pet => pet.id !== args.id)
        return pets.find(pet => pet.id === args.id)
      }
    }
  }
  
  export default resolvers