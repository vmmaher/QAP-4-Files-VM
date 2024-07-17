// let motelCustomer = {
//     name: "",
//     dateOfBirth: "",
//     gender: "",
//     roomPreference: ["early check-in", "extra bed", "extra key", "late check-out"],
//     paymentMethod: "",
//     mailingAddress: {
//         street: "",
//         city: "",
//         province: "",
//         postalCode: ""
//     },
//     phoneNumber: "",
//     checkInDate: {
//         date: "",
//         checkOutDate: ""
//     },
// }

let motelCustomer = {
    name: "Billy Bob Smith",
    dateOfBirth: "1985-06-01",
    gender: "M",
    roomPreference: ["early check-in", "extra bed", "extra key", "late check-out"],
    paymentMethod: "Credit",
    mailingAddress: {
        street: "12 Main Street",
        city: "Toronto",
        province: "ON",
        postalCode: "M4C 2J4"
    },
    phoneNumber: "7095419861",
    checkInDate: {
        date: "2024-07-14",
        checkOutDate: "2024-07-16"
    }
};

if (motelCustomer.gender === "M") {
    pronounInCaps = "He"; }
else if (motelCustomer.gender === "F") {
    pronounInCaps = "She"; }

let motelCustomerDescription = `The customer's name is ${motelCustomer.name}.
${pronounInCaps} was born on ${motelCustomer.dateOfBirth}.
The mailing address on file is ${motelCustomer.mailingAddress.street}, ${motelCustomer.mailingAddress.city}, ${motelCustomer.mailingAddress.province}, ${motelCustomer.mailingAddress.postalCode} 
The phone number on file is ${motelCustomer.phoneNumber}. 
Room preferences indicated were ${motelCustomer.roomPreference.join(', ')}. 
Check-in date was ${motelCustomer.checkInDate.date} and check-out date was ${motelCustomer.checkInDate.checkOutDate}.`;

console.log(motelCustomerDescription);
