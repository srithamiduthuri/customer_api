const apiUrl = "/api/customers";

async function fetchCustomers() {
  const res = await fetch(apiUrl + "/");
  const customers = await res.json();
  const tbody = document.getElementById("customerList");
  tbody.innerHTML = "";
  customers.forEach(c => {
    tbody.innerHTML += `
      <tr>
        <td>${c.id}</td>
        <td>${c.name}</td>
        <td>${c.email}</td>
        <td>${c.phone || ""}</td>
        <td>
          <button onclick="deleteCustomer(${c.id})">Delete</button>
          <button onclick="editCustomer(${c.id}, '${c.name}', '${c.email}', '${c.phone || ""}')">Edit</button>
        </td>
      </tr>`;
  });
}

document.getElementById("customerForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;

  await fetch(apiUrl + "/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, phone })
  });

  e.target.reset();
  fetchCustomers();
});

async function deleteCustomer(id) {
  await fetch(apiUrl + "/" + id, { method: "DELETE" });
  fetchCustomers();
}

async function editCustomer(id, name, email, phone) {
  const newName = prompt("Enter new name:", name);
  const newEmail = prompt("Enter new email:", email);
  const newPhone = prompt("Enter new phone:", phone);

  if (newName && newEmail) {
    await fetch(apiUrl + "/" + id, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: newName, email: newEmail, phone: newPhone })
    });
    fetchCustomers();
  }
}

// Initial load
fetchCustomers();
