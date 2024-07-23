// Example blank template:
//
//     name: "",
//     dateOfBirth: "",
//     gender: "",
//     roomPreference: ["early check-in", "extra bed", "extra key", "late check-out"],
//     roomNumber: "",
//     paymentMethod: "",
//     mailingAddress: {
//         street: "",
//         city: "",
//         province: "",
//         postalCode: "",
//     },
//     phoneNumber: "",
//     emailAddress: "",
//     checkInDate: "",
//     checkOutDate: "", 

let motelCustomer = {
    name: "Billy Bob Smith",
    dateOfBirth: "1985-06-01",
    gender: "M",
    roomPreference: ["extra bed", "extra key", "late check-out"],
    roomNumber: "344",
    paymentMethod: "Credit",
    mailingAddress: {
        street: "12 Main Street",
        city: "Toronto",
        province: "ON",
        postalCode: "M4C 2J4",
    },
    phoneNumber: "7095419861",
    emailAddress: "billybobsmith@gmail.com",
    checkInDate: "2024-07-14",
    checkOutDate: "2024-07-16", 

    determineStayLength: function() {
        return (new Date(this.checkOutDate) - new Date(this.checkInDate)) / (24 * 60 * 60 * 1000);
    },
    determineAge: function() {
        const birthDate = new Date(this.dateOfBirth);
        const today = new Date();
        let age = today.getFullYear() - birthDate.getFullYear();
        if (today < new Date(today.getFullYear(), birthDate.getMonth(), birthDate.getDate())) {
            age--;
        }
        return age;
    },
    determinePronoun: function() {
        if (this.gender === "M") {
            this.pronounInCaps = "He";
            this.pronounNormal = "he";
        }
        else if (this.gender === "F") {
            this.pronounInCaps = "She";
            this.pronounNormal = "she";
        }
    },
};

motelCustomer.determinePronoun();

let motelCustomerDescription = `The customer's name is ${motelCustomer.name}.
${motelCustomer.pronounInCaps} was born on ${motelCustomer.dateOfBirth}, meaning ${motelCustomer.pronounNormal} is ${motelCustomer.determineAge()} years old.
The mailing address on file is ${motelCustomer.mailingAddress.street}, ${motelCustomer.mailingAddress.city}, ${motelCustomer.mailingAddress.province}, ${motelCustomer.mailingAddress.postalCode}. 
The phone number on file is ${motelCustomer.phoneNumber}, and the email address on file is ${motelCustomer.emailAddress}. 
Room preferences indicated were ${motelCustomer.roomPreference.join(', ')}.
${motelCustomer.name} was located in room number ${motelCustomer.roomNumber}.
Check-in date was ${motelCustomer.checkInDate} and check-out date was ${motelCustomer.checkOutDate}.
The duration of the stay was ${motelCustomer.determineStayLength()} days.`;

console.log(motelCustomerDescription);
//document.write(motelCustomerDescription); //This overwrites any previous html so it is usually used for testing.// //
window.alert(motelCustomerDescription);
